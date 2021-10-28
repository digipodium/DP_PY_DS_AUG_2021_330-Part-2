from ctypes import resize
from os import name
import streamlit as st
from textblob import TextBlob
import plotly.express as px

def show_senti_str(value):
    if value > 0:
        return 'postive 😁'
    elif value < 0:
        return 'negative 😡'
    else :
        return 'neutral 😶'
    

st.title("Simple Sentiment Analysis")

with st.form("f1"):
    message = st.text_area("Enter you message",height=500)
    style = st.checkbox("do sentence wise analysis?")
    btn = st.form_submit_button("Analyse message")

if btn and message:
    if not style:
        blob = TextBlob(message)
        out = blob.sentiment.polarity
        out = show_senti_str(out)
        st.info(out)
    else:
        blob = TextBlob(message)
        result = {}
        for sentence in blob.sentences:
            val = sentence.sentiment.polarity
            val = show_senti_str(val)
            if val in result:
                result[val] += 1
            else:
                result[val] = 1
        st.write(result)
        fig =  px.pie(
                    names=['postive 😁','negative 😡','neutral 😶'],
                    values=[result.get('postive 😁'),
                            result.get('negative 😡'),
                            result.get('neutral 😶')],
                    title="Sentence wise sentiment analysis"
                    )
        st.plotly_chart(fig)
    

