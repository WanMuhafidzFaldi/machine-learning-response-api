# 1. Contoh DataUji  
# dataUji = [
#     {"responseData": '{"email": "user@example.com"}', "scoringData": 2},  
#     {"responseData": '{"pic": "john@company.com"}', "scoringData": 2},  
#     {"responseData": '{"alamat": "Jakarta Selatan"}', "scoringData": 2},  
#     {"responseData": '{"email": "00542025-754c-4446-9030-22758938cc3b"}', "scoringData": 1},
#     {"responseData": '{"steel":"knife","anybody":"environment","dirt":"afternoon","twenty":true,"lady":false,"struck":"compound"}', "scoringData": 0},
#     {"responseData": '{"scene":-699625218,"along":1278992754,"start":true,"mind":"mark","perhaps":{"knife":1854340532,"stove":{"advice":true,"him":"exciting","selection":"roll","seeing":true,"slipped":-1818490715.8282523,"brave":false},"occasionally":"supper","single":"pan","threw":true,"volume":"kill"},"pressure":"apart"}', "scoringData": 0},
#     {"responseData": '{"known":1435401701.0544872,"most":{"neck":-1081584193.9818058,"knowledge":"negative","art":{"construction":-1029749549,"bound":true,"field":"flame","no":true,"win":260693246,"very":"youth"},"younger":"early","mean":-2048932268,"below":false},"jack":"replace","wing":"outer","outline":"excellent","nearby":true}', "scoringData": 0},
#     {"responseData": '{"damage":"be","birth":"mirror","speech":true,"grandfather":true,"forgotten":"individual","guess":"company"}', "scoringData": 0},
#     {"responseData": '{"passportId":"665de1f2775ca0b64d3ceda7c1b4bd15e32a73ed","discount":{"price":"20.00"},"supplier":"est","dateOfBirth":"729359e8bcfa61b5595f86a11c57ea09d09617b1","batchNumber":"non","qrCode":{"discount":{"modelNumber":"vero"}},"location":"incidunt","warranty":"3 years","rating":{"maritalStatus":"repellat","socialMediaProfile":"61f611a4fd585e96d518c703dc7dcdeec8354e1c"},"website":{"store":{"policyNumber":"a5bc1d9b2ae74e7a8a249659c13b14f5c2eac13f"}}}', "scoringData": 2},
#     # Tambahkan lebih banyak data sesuai kebutuhan  
# ]
import json

def loadDataTest(filePath):
    with open(filePath, 'r') as file:
        data = json.load(file)
  
    dataTest = []
    for entry in data:
        logs = entry.get('logs', {})
        responseData = logs.get('data', {})
        keyValueLabels = logs.get('keyValueLabels', [])
  
        maxScoringData = max((kv[2] for kv in keyValueLabels if len(kv) > 2), default=None)
  
        # Ubah responseData menjadi string JSON
        if isinstance(responseData, (list, dict)):
          responseData = json.dumps(responseData)
  
        dataTest.append({
          'responseData': responseData,
          'scoringData': maxScoringData
        })

    return dataTest
