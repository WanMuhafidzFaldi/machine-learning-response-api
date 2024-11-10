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
