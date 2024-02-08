import streamlit as st
from langchain.document_loaders import OnlinePDFLoader

loader = OnlinePDFLoader("https://www.colegioemaus.edu.ar/assets/tragedias_shakespeare.pdf")
document = loader.load()
