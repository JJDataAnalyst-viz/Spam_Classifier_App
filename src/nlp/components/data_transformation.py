from src.nlp.components.data_ingestion import ingest_data
from string import punctuation
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re
import nltk

nltk.download('wordnet',quiet=True)
nltk.download('stopwords',quiet=True)

def transform_data():
    corpus = []
    lemma_ = WordNetLemmatizer()
    df = ingest_data()
    X = df.iloc[:,0]
    y = df.iloc[:,-1]
    for i in range(len(X)):
        review = re.sub('[^a-zA-Z]'," ",X.iloc[i])
        review = review.lower()
        review = review.split()
        review = [lemma_.lemmatize(word) for word in review if word not in punctuation and word not in stopwords.words('english')]
        review = " ".join(review)
        corpus.append(review)
    return corpus


if __name__ == "__main__":
    print(len(transform_data()))

