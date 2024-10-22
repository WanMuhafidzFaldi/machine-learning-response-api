from sklearn.svm import LinearSVC  
from sklearn.metrics import classification_report  
import json

def machineLearning(xTrain, xTest, yTrain, yTest):
  # 5. Melatih Model SVM  
  model = LinearSVC()  
  model.fit(xTrain, yTrain)

  # 6. Prediksi dan Evaluasi  
  yPred = model.predict(xTest)  
  print(classification_report(yTest, yPred, zero_division=0))  

  return model


# 7. Fungsi untuk Memprediksi PII dalam Respons API Baru  
def predictPii(model, vectorizer, response):  
    
    try:  
        response_dict = json.loads(response)  
    except json.JSONDecodeError:  
        return "Invalid JSON"  
    
    response_text = json.dumps(response_dict)  
    response_vectorized = vectorizer.transform([response_text])  
    prediction = model.predict(response_vectorized)  
    print(prediction)
    return "Contains PII" if prediction[0] == 1 else "Does not contain PII"  
