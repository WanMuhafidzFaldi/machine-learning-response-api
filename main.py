from data_processing import dataProcessing
from data_set import loadDataTraining
from data_uji import loadDataTest
from machine_learning import machineLearning
from machine_learning import predictPii
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, confusion_matrix

filePathDataSet = 'dataset1.json'
dataSet = loadDataTraining(filePathDataSet)
xTrain, xTest, yTrain, yTest, vectorizer = dataProcessing(dataSet)

model = machineLearning(xTrain, xTest, yTrain, yTest)

# List untuk menyimpan hasil prediksi dan label sebenarnya
yTrue = []
yPred = []

filePathDataTest = 'datauji1.json'
dataTest = loadDataTest(filePathDataTest)
for data in dataTest:
    print("Data Uji: ", data['responseData'])
    print("Scoring Seharusnya: ", data['scoringData'])
    predict, textReport = predictPii(model, vectorizer, data['responseData'])  # Output: Does not contain PII
    print("Hasil Prediksi: ", predict)
    print("Text Report: ", textReport)
    print("\n")

    # Simpan hasil prediksi dan label sebenarnya
    yTrue.append(data['scoringData'])
    yPred.append(predict)

# Hitung metrik-metrik
accuracy = accuracy_score(yTrue, yPred)
f1 = f1_score(yTrue, yPred, average='weighted')
precision = precision_score(yTrue, yPred, average='weighted')
recall = recall_score(yTrue, yPred, average='weighted')
conf_matrix = confusion_matrix(yTrue, yPred)

print(f"Akurasi: {accuracy}")
print(f"F1-score: {f1}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"Confusion Matrix: \n{conf_matrix}")