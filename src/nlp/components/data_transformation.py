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
import joblib
import pandas as pd
import yaml
import os
from src.nlp.utils.common import safe_to_joblib


with open('config/params.yaml', 'r') as f:
    params = yaml.safe_load(f)['SPLIT_DATA']

df = ingest_data()
def transform_data(df : pd.DataFrame ):
    
    corpus = []
    encoder = LabelEncoder()
    lemma_ = WordNetLemmatizer()
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
  
    safe_to_joblib(encoder,'models/encoder.pkl')
   
    X_train,X_test,y_train,y_test = train_test_split(corpus,y_encoded,test_size=params['TEST_SIZE'])
    return  X_train,X_test,y_train,y_test


if __name__ == "__main__":
    X_train,X_test,y_train,y_test = transform_data()
    
