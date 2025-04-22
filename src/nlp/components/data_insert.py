import psycopg2 
import dotenv
import os
import pandas as pd
dotenv.load_dotenv('.env')

def insert_data():
    df = pd.read_csv('data/training_data/spamhamdata.csv',sep='	',encoding='utf-8',header = None,names = ['Output','Text'])
    conn = psycopg2.connect(
        database = os.getenv('PYDB'),
        host = os.getenv('PYHOST'),
        password = os.getenv('PYPASSWORD'),
        user = os.getenv('PYUSERNAME'),
        port = os.getenv('PYPORT'))

    cursor = conn.cursor() 
    list_data = df[['Output','Text']].values.tolist()
    insert_query = (f'INSERT INTO NLP (OUTPUT_TEXT,INPUT_TEXT) VALUES(%s,%s)')

    cursor.executemany(insert_query,list_data)

    conn.commit()

    conn.close()


if __name__ == "__main__":
    insert_data()