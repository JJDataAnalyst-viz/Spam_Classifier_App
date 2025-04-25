from sklearn.feature_extraction.text import TfidfVectorizer
from src.nlp.components.data_transformation import transform_data
from xgboost import XGBClassifier
from sklearn.metrics import confusion_matrix
import joblib
import yaml 
from src.nlp.utils.common import load_yaml_file
from src.nlp.utils.common import safe_to_joblib

def modeling_data(X_train,X_test,y_train,y_test):
    
    params = load_yaml_file('MODEL_PARAMS')

    vectorizer = TfidfVectorizer(ngram_range=tuple(params['TFIDF_RANGE']))

    X_train_vect = vectorizer.fit_transform(X_train)
 
    X_test_vect = vectorizer.transform(X_test) 

    xgb = XGBClassifier(eta = params['ETA'],max_depth = params['MAX_DEPTH'])
    xgb.fit(X_train_vect,y_train)

    results = xgb.predict(X_test_vect)
  
    safe_to_joblib(xgb,'models/xgb_model.pkl')
    safe_to_joblib(vectorizer,'models/vectorizer.pkl')
    return confusion_matrix(y_test,results)




if __name__ == "__main__":
    results = modeling_data()
   

     