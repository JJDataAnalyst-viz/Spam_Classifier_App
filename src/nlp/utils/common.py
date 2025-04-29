import psycopg2
import os
import dotenv
import yaml

import pickle
from typing import List
from src.nlp.constants import PARAMS_YAML,CONFIG_YAML
dotenv.load_dotenv('.env')


def connect_to_database(query : str,insert : bool = False,fetchone: bool = True):
    conn = psycopg2.connect(
    database=os.getenv('PYDB'),
    host=os.getenv('PYHOST'),
    password=os.getenv('PYPASSWORD'),
    user=os.getenv('PYUSERNAME'),
    port=os.getenv('PYPORT_')
)
    cursor = conn.cursor()
 

    if insert:
        pass
    else:
        cursor.execute(str(query))
        if fetchone:
            return cursor.fetchone()
        else:
            return cursor.fetchall()

    conn.close()





def load_yaml_file(extension: List):
    with open(PARAMS_YAML,'r') as file:
        params = yaml.safe_load(file)[extension]

    return params


def safe_to_joblib(name, file_path):
    with open(file_path, 'wb') as f:  # Otwieramy plik w trybie binarnym
        pickle.dump(name, f)