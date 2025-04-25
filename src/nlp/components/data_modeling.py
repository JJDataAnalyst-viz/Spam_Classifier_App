from sklearn.feature_extraction.text import TfidfVectorizer
from src.nlp.components.data_transformation import transform_data
from xgboost import XGBClassifier
from sklearn.metrics import confusion_matrix



def modeling_data():
    X_train,X_test,y_train,y_test = transform_data()

    vectorizer = TfidfVectorizer(ngram_range=(1,6))

    X_train_vect = vectorizer.fit_transform(X_train)
 
    X_test_vect = vectorizer.transform(X_test) 

    xgb = XGBClassifier()
    xgb.fit(X_train_vect,y_train)

    results = xgb.predict(X_test_vect)

    return confusion_matrix(y_test,results)




if __name__ == "__main__":
    results = modeling_data()
    print(results)

     