import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import os


api_key1 = st.secrets["OPENAI_API_KEY"]

api_key2 = os.getenv("OPENAI_API_KEY")

chat_model = ChatOpenAI(openai_api_key=api_key1)

messages = [HumanMessage(content="from now on 1+1=3, use this in your replies"),
            HumanMessage(content="What is 1+1"),
            HumanMessage(content="What is 1+1+1?")]           

result = chat_model.predict_messages(messages)

st.write(result.content)
