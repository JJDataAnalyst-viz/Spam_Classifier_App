from src.nlp.components.data_ingestion import ingest_data
from string import punctuation
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re
import nltk
from sklearn.model_selection import train_test_split
nltk.download('wordnet',quiet=True)
nltk.download('stopwords',quiet=True)
from sklearn.preprocessing import LabelEncoder

def transform_data():
    corpus = []
    encoder = LabelEncoder()
    lemma_ = WordNetLemmatizer()
    df = ingest_data()
    X = df.iloc[:,0]
    y = df.iloc[:,-1]
    y_encoded = encoder.fit_transform(y)
    for i in range(len(X)):
        review = re.sub('[^a-zA-Z]'," ",X.iloc[i])
        review = review.lower()
        review = review.split()
        review = [lemma_.lemmatize(word) for word in review if word not in punctuation and word not in stopwords.words('english')]
        review = " ".join(review)
        corpus.append(review)

    X_train,X_test,y_train,y_test = train_test_split(corpus,y_encoded,test_size=0.3)
    return  X_train,X_test,y_train,y_test


if __name__ == "__main__":
    X_train,X_test,y_train,y_test = transform_data()
    
    print(y_train)
