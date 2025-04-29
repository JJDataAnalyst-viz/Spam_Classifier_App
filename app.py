import streamlit as st
import pickle
import re
from nltk.stem import WordNetLemmatizer
from string import punctuation
from nltk.corpus import stopwords
from src.nlp.utils.common import connect_to_database
import uuid
lemma_ = WordNetLemmatizer()
import psycopg2
import os

conn = psycopg2.connect(
    database=os.getenv('PYDB'),
    host=os.getenv('PYHOST'),
    password=os.getenv('PYPASSWORD'),
    user=os.getenv('PYUSERNAME'),
    port=os.getenv('PYPORT_')
)
cursor = conn.cursor() 



st.title('NLP SPAM/HAM')
st.sidebar.header('NLP with NLTK and XGBOOST')

if 'inputer' not in st.session_state:
    st.session_state.inputer = ""



st.session_state.inputer = st.text_input(
    'Check if my model recognize your text as spam or ham',
    value=st.session_state.inputer
)

inputer = st.session_state.inputer  # lokalna zmienna do użycia

with open('models/encoder.pkl', 'rb') as file1:
    encoder = pickle.load(file1)

with open('models/vectorizer.pkl', 'rb') as file2:
    vectorizer = pickle.load(file2)

with open('models/xgb_model.pkl', 'rb') as file3:
    model = pickle.load(file3)

corpus = []
if inputer:

    review = re.sub('[^a-zA-Z]', " ", inputer)
    review = review.lower()
    review = review.split()

 
    review = [lemma_.lemmatize(word) for word in review if word not in punctuation and word not in stopwords.words('english')]

   
    corpus.append(" ".join(review))


    st.write("Przetworzony tekst:")
    st.write(corpus)

    result = model.predict(vectorizer.transform(corpus))
    shared_uuid = uuid.uuid1()

    if result[0] == 1:
        st.write('This is SPAM')
    else:
        st.write('This is HAM')
 
    if 'voted' not in st.session_state:
        st.session_state.voted = False

   
    col1, col2 = st.columns(2)
    with col1:
        false_answer = st.button("Model's output is invalid")
    with col2:
        true_answer = st.button("Model output is okay")

    query = 'INSERT INTO client_input (ID, INPUT_TEXT) VALUES (%s, %s)'
    cursor.execute(query, (str(shared_uuid), inputer))
    if not st.session_state.voted and (true_answer or false_answer):

        feedback = True if true_answer else False
        query = 'INSERT INTO client_review (id_review, review) VALUES (%s, %s)'
        cursor.execute(query, (str(shared_uuid), feedback))

        conn.commit()
        st.session_state.voted = True  

        st.success("Your feedback has been submitted. Thank you!")

    elif st.session_state.voted:
        st.info("You have already submitted your feedback.")

        conn.close()
clear_session = st.button('Clear state and send data one more time')
if clear_session:
        st.session_state.voted = False
        st.session_state.inputer = ""
      