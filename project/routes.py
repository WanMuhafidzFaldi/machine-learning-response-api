from flask import request, jsonify
# from project.usecases.user_usecase import UserUseCase
from project.usecases.log_usecase import LogUseCase
from project.usecases.predict_usecase import PredictUseCase
from project.database import get_db, check_connection

def register_routes(app):

    @app.route('/logs', methods=['GET'])
    def get_all_logs():
        db = get_db()
        log_usecase = LogUseCase(db)
        logs = log_usecase.get_all_logs()
        return jsonify(logs), 200
    
    @app.route('/predict/svm', methods=['POST'])
    def post_predict_svm():
        db = get_db()
        predict_usecase = PredictUseCase(db)
        data = request.get_json()
        endpoint = data.get('requestPath')
        headers = data.get('headers')
        response = data.get('data')  # Pass the entire data object as response
        # Insert request data into the database
        result = predict_usecase.save_predict_pii_svm(endpoint, headers, response)
        return jsonify({'message': 'Request data inserted successfully', 'result': result}), 200

    @app.route('/predict/naive-bayes', methods=['POST'])
    def post_predict_naive_bayes():
        db = get_db()
        predict_usecase = PredictUseCase(db)
        data = request.get_json()
        endpoint = data.get('requestPath')
        headers = data.get('headers')
        response = data.get('data')  # Pass the entire data object as response
        # Insert request data into the database
        result = predict_usecase.save_predict_pii_naive_bayes(endpoint, headers, response)
        return jsonify({'message': 'Request data inserted successfully', 'result': result}), 200
    
    @app.route('/predict/svm', methods=['GET'])
    def get_predict_pii():
        db = get_db()
        log_usecase = LogUseCase(db)
        logs = log_usecase.get_predict_pii_svm()
        return jsonify(logs), 200

    @app.route('/predict/naive-bayes', methods=['GET'])
    def get_predict_naive_bayes():
        db = get_db()
        log_usecase = LogUseCase(db)
        logs = log_usecase.get_predict_pii_naive_bayes()
        return jsonify(logs), 200
    

    @app.route('/health', methods=['GET'])
    def health_check():
        if check_connection():
            return jsonify({"status": "UP"}), 200
        else:
            return jsonify({"status": "DOWN"}), 500