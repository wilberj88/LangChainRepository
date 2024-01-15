import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema import BaseOutputParser
import os


api_key1 = st.secrets["OPENAI_API_KEY"]

chat_model = ChatOpenAI(openai_api_key=api_key1)

class CommaSeparatedListOutputParser(BaseOutputParser):
  def parse(self, text: str):
    return text.strip().split(", ")

template = """You area helpful assitant who generates comma separated lists.
a user will pass in a category, and you should generate 5 objects in that category in a comma separated list.
ONLY return a commma separated list, and nothing more."""
human_template = "{text}"

chat_prompt = ChatPromptTemplate.from_messages([
  ("system", template),
  ("human", human_template),
])

chain = chat_prompt | chat model | CommaSeparatedListOutputParser()
result = chain.invoke({"text": "colors"})
st.write(result)
