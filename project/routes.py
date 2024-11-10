from flask import request, jsonify
# from project.usecases.user_usecase import UserUseCase
from project.usecases.log_usecase import LogUseCase
from project.database import get_db, check_connection

def register_routes(app):

    @app.route('/logs', methods=['GET'])
    def get_all_logs():
        db = get_db()
        log_usecase = LogUseCase(db)
        logs = log_usecase.get_all_logs()
        return jsonify(logs), 200
    
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