import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema import BaseOutputParser
import os


api_key1 = st.secrets["OPENAI_API_KEY"]

class AnswerOutputParser(BaseOutputParser):
  def parse(self, text: str):
    """Parse the output of an LLM call."""
    return text.strip().split("answer =")


chat_model = ChatOpenAI(openai_api_key=api_key1)

template = """You area helpful assitant that solves math problems and shows your work.
            Output each step then return the answer in the folowing format: answer = <answer here>.
            Make sure to output answer in all lowercases and to have exactly one space and one equal sign following it.
           """
human_template = "{problem}"

chat_prompt = ChatPromptTemplate.from_messages([
  ("system", template),
  ("human", human_template),
])

messages = chat_prompt.format_messages(problem="haz la serie de fibonacci para los primeros 6 números")
result = chat_model.predict_messages(messages)
parsed = AnswerOutputParser().parse(result.content)
steps, answer = parsed

st.write(steps)
