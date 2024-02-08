import streamlit as st
from langchain.document_loaders import OnlinePDFLoader

loader = OnlinePDFLoader("https://arxiv.org/pdf/1911.01547.pdf")
document = loader.load()
