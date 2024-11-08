# # 1. Contoh Dataset  
# dataSet = [
#     {"responseData": '{"email": "user@example.com"}', "scoringData": 2},  
#     {"responseData": '{"pic": "john@company.com"}', "scoringData": 2},  
#     {"responseData": '{"alamat": "Jakarta Selatan"}', "scoringData": 2},  
#     {"responseData": '{"fullName": "Ahmad"}', "scoringData": 2},  
#     {"responseData": '{"phoneNumber": "08512312312"}', "scoringData": 2},
#     {"responseData": '{"email": "00542025-754c-4446-9030-22758938cc3b"}', "scoringData": 1},
#     {"responseData": '{"productName": "Mangga Goreng"}', "scoringData": 0},
#     {"responseData": '{"productName": "Mangga Goreng"}', "scoringData": 0},
#     {"responseData": '{"email": "00542025-754c-4446-9030-22758938cc3b"}', "scoringData": 1},
#     {"responseData": '{"fullName": "Ahmad"}', "scoringData": 2},
#     {"responseData": '{"productName": "Apel Mentega"}', "scoringData": 0},
#     {"responseData": '{"email": "44423456-7890-4567-8901-345678901234"}', "scoringData": 1},
#     {"responseData": '{"fullName": "Budi"}', "scoringData": 2},
#     {"responseData": '{"productName": "Pisang Keju"}', "scoringData": 0},
#     {"responseData": '{"email": "55534567-8901-4567-8901-456789012345"}', "scoringData": 1},
#     {"responseData": '{"fullName": "Citra"}', "scoringData": 2},
#     {"responseData": '{"productName": "Nasi Goreng"}', "scoringData": 0},
#     {"responseData": '{"email": "66645678-9012-4567-8901-567890123456"}', "scoringData": 1},
#     {"responseData": '{"fullName": "Denny"}', "scoringData": 2},
#     {"responseData": '{"scene":-699625218,"along":1278992754,"start":true,"mind":"mark","perhaps":{"knife":1854340532,"stove":{"advice":true,"him":"exciting","selection":"roll","seeing":true,"slipped":-1818490715.8282523,"brave":false},"occasionally":"supper","single":"pan","threw":true,"volume":"kill"},"pressure":"apart"}', "scoringData": 0},
#     {"responseData": '{"known":1435401701.0544872,"most":{"neck":-1081584193.9818058,"knowledge":"negative","art":{"construction":-1029749549,"bound":true,"field":"flame","no":true,"win":260693246,"very":"youth"},"younger":"early","mean":-2048932268,"below":false},"jack":"replace","wing":"outer","outline":"excellent","nearby":true}', "scoringData": 0},
#     {"responseData": '{"damage":"be","birth":"mirror","speech":true,"grandfather":true,"forgotten":"individual","guess":"company"}', "scoringData": 0},
#     {"responseData": '{"steel":"knife","anybody":"environment","dirt":"afternoon","twenty":true,"lady":false,"struck":"compound"}', "scoringData": 0},
#     # Tambahkan lebih banyak data sesuai kebutuhan  
# ]  
import json

def loadDataTraining(filePath):
    with open(filePath, 'r') as file:
        data = json.load(file)
    
    dataSet = []
    for entry in data:
        logs = entry.get('logs', {})
        keyValueLabels = logs.get('keyValueLabels', [])
        
        for kv in keyValueLabels:
            if len(kv) >= 3:
                responseData = {kv[0]: kv[1]}
                scoringData = kv[2]
                dataSet.append({
                    'responseData': json.dumps(responseData),
                    'scoringData': scoringData
                })
    
    return dataSet
