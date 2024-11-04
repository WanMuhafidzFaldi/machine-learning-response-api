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
        responseDict = json.loads(response)  
    except json.JSONDecodeError:  
        return "Invalid JSON"  
    
    responseText = json.dumps(responseDict)  
    responseVectorized = vectorizer.transform([responseText])  
    prediction = model.predict(responseVectorized)
    if prediction[0] == 0:
        return prediction[0], "Key: Not PII, Value: Not PII"
    elif prediction[0] == 1:
        return prediction[0], "Key: PII, Value: Random Data"
    elif prediction[0] == 2:
        return prediction[0], "Key: PII, Value: PII Data"
    else:
        return prediction[0], "Unknown Prediction"
