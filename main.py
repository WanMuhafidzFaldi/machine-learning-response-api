import json 
from sklearn.svm import LinearSVC  
from sklearn.metrics import classification_report  
from data_processing import dataProcessing
from data_set import dataSet
from machine_learning import machineLearning
from machine_learning import predictPii

xTrain, xTest, yTrain, yTest, vectorizer = dataProcessing(dataSet)

model = machineLearning(xTrain, xTest, yTrain, yTest)



# # Contoh Penggunaan  
new_response_1 = '''  
{  
  "products": [  
    {  
      "id": 101,  
      "title": "Apple AirPods Max Silver",  
      "category": "mobile-accessories"  
    }  
  ],  
  "total": 23,  
  "skip": 0,  
  "limit": 23  
}  
'''  

new_response_2 = '''  
{  
  "email": "asdfasdfdsfds",  
  "fullName": "asdfasdf",  
  "phoneNumber": "asdfasfdsfs",  
  "products": [  
    {  
      "id": 101,  
      "title": "Apple AirPods Max Silver",  
      "category": "mobile-accessories"  
    }  
  ],  
  "total": 23,  
  "skip": 0,  
  "limit": 23  
}  
''' 

print(predictPii(model, vectorizer, new_response_1))  # Output: Does not contain PII  
print(predictPii(model, vectorizer, new_response_2))  # Output: Contains PII  