
import json

# 7. Fungsi untuk Memprediksi PII
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
