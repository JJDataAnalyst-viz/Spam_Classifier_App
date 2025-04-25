import streamlit as st


st.title('NLP SPAM/HAM')
st.sidebar.header('NLP with NLTK and XGBOOST')
input = st.text_input('Check if my model recognize your text as spam or ham')

if input:
    st.write('well done')
 

