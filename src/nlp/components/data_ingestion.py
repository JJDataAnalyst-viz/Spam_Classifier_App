import psycopg2
import os
import dotenv
import pandas as pd
from src.nlp.utils.common import connect_to_database

dotenv.load_dotenv('.env')

def ingest_data():
    return pd.DataFrame(connect_to_database('Select input_text,output_text FROM NLP',False,False),columns=['Text','Output'])

if __name__ == "__main__":
    ingest_data()