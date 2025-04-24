import psycopg2
import os
import dotenv
dotenv.load_dotenv('.env')


def connect_to_database(query : str,insert : bool = False,fetchone: bool = True):
    conn = psycopg2.connect(
        database = os.getenv('PYDB'),
            host = os.getenv('PYHOST'),
            password = os.getenv('PYPASSWORD'),
            user = os.getenv('PYUSERNAME'),
            port = os.getenv('PYPORT'))

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

