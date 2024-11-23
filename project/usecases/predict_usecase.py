from project.repositories.detection_result_repository import DetectionResultRepository
from project.utils import predict_pii
import os
import joblib
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, confusion_matrix
from flask import current_app
import numpy as np
import json

class PredictUseCase:
    def __init__(self, db):
        self.detection_result_repository = DetectionResultRepository(db)

    def save_predict_pii_svm(self, endpoint, headers, response):
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
        
        predict, textReport = predict_pii.predictPii(model, vectorizer, json.dumps(response))  # Output: Does not contain PII
        # Convert NumPy int64 to regular Python int
        if isinstance(predict, np.int64):
            predict = int(predict)
        
        
        # Determine severity based on conditions
        authorization_exists = 'authorization' in headers
        
        if authorization_exists and predict == 1:
            severity = "Pass"
        elif not authorization_exists and predict == 0:
            severity = "Pass"
        elif authorization_exists and predict == 2:
            severity = "Warning"
        elif not authorization_exists and predict == 1:
            severity = "Warning"
        elif not authorization_exists and predict == 2:
            severity = "Critical"
        else:
            severity = "Unknown"

        saveData = self.detection_result_repository.save({
            "model": "svm",
            "endpoint": endpoint,
            "authorization": authorization_exists,
            "predict": predict,
            "severity": severity,
            "response": response,
        })
        print(saveData)
        
        # Prepare the result as a dictionary
        result = {
            "Endpoint": endpoint,
            "authorization": authorization_exists,
            "Hasil Prediksi": predict,
            "Text Report": textReport,
            "Severity": severity,
            "response": response,
        }

        return result
    
    def save_predict_pii_naive_bayes(self, endpoint, headers, response):
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
        
        predict, textReport = predict_pii.predictPii(model, vectorizer, json.dumps(response))  # Output: Does not contain PII
        # Convert NumPy int64 to regular Python int
        if isinstance(predict, np.int64):
            predict = int(predict)
        
        
        # Determine severity based on conditions
        authorization_exists = 'authorization' in headers
        
        if authorization_exists and predict == 1:
            severity = "Pass"
        elif not authorization_exists and predict == 0:
            severity = "Pass"
        elif authorization_exists and predict == 2:
            severity = "Warning"
        elif not authorization_exists and predict == 1:
            severity = "Warning"
        elif not authorization_exists and predict == 2:
            severity = "Critical"
        else:
            severity = "Unknown"

        saveData = self.detection_result_repository.save({
            "model": "naive_bayes",
            "endpoint": endpoint,
            "authorization": authorization_exists,
            "predict": predict,
            "severity": severity,
            "textReport": textReport,
            "response": response,
        })
        print(saveData)
        
        # Prepare the result as a dictionary
        result = {
            "Endpoint": endpoint,
            "authorization": authorization_exists,
            "Hasil Prediksi": predict,
            "Text Report": textReport,
            "Severity": severity,
            "response": response,
        }

        return result
