from sklearn.svm import LinearSVC  
from sklearn.metrics import classification_report  
from sklearn.feature_extraction.text import TfidfVectorizer  
from sklearn.model_selection import train_test_split

def dataProcessing(data):

    # 2. Memisahkan teks dan label  
    responseData = [item['responseData'] for item in data]  
    scoringData = [item['scoringData'] for item in data]
    # 3. Vectorisasi Teks dengan TF-IDF  
    vectorizer = TfidfVectorizer(max_features=1000, ngram_range=(1,2))  
    x = vectorizer.fit_transform(responseData)  
    y = scoringData

    # 4. Membagi Data menjadi Training dan Testing Set  
    xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.2, random_state=42)  
    
    return xTrain, xTest, yTrain, yTest, vectorizer