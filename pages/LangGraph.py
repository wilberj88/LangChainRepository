import streamlit as st
from openai import OpenAI
from langchain.chat_models import ChatOpenAI

api_key1 = st.secrets["OPENAI_API_KEY"]

chat_model = ChatOpenAI(openai_api_key=api_key1)

client = OpenAI(api_key=api_key1)

