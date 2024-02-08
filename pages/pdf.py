import streamlit as st
import pypdf
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("data/E24AlcaldiaBog2019.pdf")
pages = loader.load_and_split()

st.write(pages)
