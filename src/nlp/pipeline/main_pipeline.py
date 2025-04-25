from src.nlp.components.data_ingestion import ingest_data
from src.nlp.components.data_transformation import transform_data
from src.nlp.components.data_modeling import modeling_data
# from datetime import datetime
# from airflow import DAG,task
# import pendulum
# import json


if __name__ == "__main__":
    df = ingest_data()
    X_train,X_test,y_train,y_test =  transform_data(df)
    results = modeling_data(X_train,X_test,y_train,y_test)
    print(results)