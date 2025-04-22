import psycopg2
import os
import dotenv
dotenv.load_dotenv('.env')

conn = psycopg2.connect(
     database = os.getenv('PYDB'),
        host = os.getenv('PYHOST'),
        password = os.getenv('PYPASSWORD'),
        user = os.getenv('PYUSERNAME'),
        port = os.getenv('PYPORT'))

cursor = conn.cursor()

conn.close()
