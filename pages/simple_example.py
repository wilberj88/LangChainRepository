import streamlit as st
from langchain.chat_models import ChatOpenAI
import os


api_key1 = st.secrets["OPENAI_API_KEY"]

api_key2 = os.getenv("OPENAI_API_KEY")

chat_model = ChatOpenAI(openai_api_key=api_key1)

result = chat_model.predict("Hola dime que es python")

st.write(result)
