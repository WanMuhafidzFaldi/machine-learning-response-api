from project.repositories.log_repository import LogRepository
from project.utils import predict_pii, data_uji
import os
import joblib
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, confusion_matrix
from flask import current_app
import json

class LogUseCase:
    def __init__(self, db):
        self.log_repository = LogRepository(db)

    def get_logs_by_request_path(self, request_path):
        logs = self.log_repository.get_logs_by_request_path(request_path)
        return logs

    def get_all_logs(self):
        logs = self.log_repository.get_all_logs()
        return logs

    def get_predict_pii_svm(self):
        # List untuk menyimpan hasil prediksi dan label sebenarnya
        yTrue = []
        yPred = []

        # Build the absolute path for the model and vectorizer files
        model_path = os.path.join(current_app.root_path, 'project' ,'models', 'model_svm.pkl')
        vectorizer_path = os.path.join(current_app.root_path, 'project' ,'models', 'vectorizer.pkl')

        # Load the trained model
        try:
            model = joblib.load(model_path)
        except FileNotFoundError:
            print("Error: The model file was not found. Please train the model first.")
            exit(1)

        # Load the vectorizer
        try:
            vectorizer = joblib.load(vectorizer_path)
        except FileNotFoundError:
            print("Error: The vectorizer file was not found. Please train the model first.")
            exit(1)
        
        filePathDataTest = os.path.join(current_app.root_path, 'project' ,'utils', 'datauji1.json') 
        dataTest = data_uji.loadDataTest(filePathDataTest)

        for data in dataTest:
            print("Data Uji: ", data['responseData'])
            print("Scoring Seharusnya: ", data['scoringData'])
            predict, textReport = predict_pii.predictPii(model, vectorizer, data['responseData'])  # Output: Does not contain PII
            print("Hasil Prediksi: ", predict)
            print("Text Report: ", textReport)
            print("\n")

            # Simpan hasil prediksi dan label sebenarnya
            yTrue.append(data['scoringData'])
            yPred.append(predict)

        # Hitung metrik-metrik
        totalData = len(dataTest)  
        accuracy = accuracy_score(yTrue, yPred)
        f1 = f1_score(yTrue, yPred, average='weighted')
        precision = precision_score(yTrue, yPred, average='weighted')
        recall = recall_score(yTrue, yPred, average='weighted')
        conf_matrix = confusion_matrix(yTrue, yPred)

        # Prepare the result as a dictionary
        result = {
            "Jumlah Data Uji": totalData,
            "Akurasi": accuracy,
            "F1-score": f1,
            "Precision": precision,
            "Recall": recall,
            "Confusion Matrix": conf_matrix.tolist()  # Convert numpy array to list
        }

        return result
    
    def get_predict_pii_naive_bayes(self):
        # List untuk menyimpan hasil prediksi dan label sebenarnya
        yTrue = []
        yPred = []

        # Build the absolute path for the model and vectorizer files
        model_path = os.path.join(current_app.root_path, 'project' ,'models', 'model_naive_bayes.pkl')
        vectorizer_path = os.path.join(current_app.root_path, 'project' ,'models', 'vectorizer.pkl')

        # Load the trained model
        try:
            model = joblib.load(model_path)
        except FileNotFoundError:
            print("Error: The model file was not found. Please train the model first.")
            exit(1)

        # Load the vectorizer
        try:
            vectorizer = joblib.load(vectorizer_path)
        except FileNotFoundError:
            print("Error: The vectorizer file was not found. Please train the model first.")
            exit(1)
        
        filePathDataTest = os.path.join(current_app.root_path, 'project' ,'utils', 'datauji1.json') 
        dataTest = data_uji.loadDataTest(filePathDataTest)

        for data in dataTest:
            print("Data Uji: ", data['responseData'])
            print("Scoring Seharusnya: ", data['scoringData'])
            predict, textReport = predict_pii.predictPii(model, vectorizer, data['responseData'])  # Output: Does not contain PII
            print("Hasil Prediksi: ", predict)
            print("Text Report: ", textReport)
            print("\n")

            # Simpan hasil prediksi dan label sebenarnya
            yTrue.append(data['scoringData'])
            yPred.append(predict)

        # Hitung metrik-metrik
        totalData = len(dataTest)  
        accuracy = accuracy_score(yTrue, yPred)
        f1 = f1_score(yTrue, yPred, average='weighted')
        precision = precision_score(yTrue, yPred, average='weighted')
        recall = recall_score(yTrue, yPred, average='weighted')
        conf_matrix = confusion_matrix(yTrue, yPred)

        # Prepare the result as a dictionary
        result = {
            "Jumlah Data Uji": totalData,
            "Akurasi": accuracy,
            "F1-score": f1,
            "Precision": precision,
            "Recall": recall,
            "Confusion Matrix": conf_matrix.tolist()  # Convert numpy array to list
        }

        return result