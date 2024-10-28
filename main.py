from data_processing import dataProcessing
from data_set import dataSet
from data_uji import dataUji
from machine_learning import machineLearning
from machine_learning import predictPii

xTrain, xTest, yTrain, yTest, vectorizer = dataProcessing(dataSet)

model = machineLearning(xTrain, xTest, yTrain, yTest)

for data in dataUji:
    print(predictPii(model, vectorizer, data['responseData']))  # Output: Does not contain PII