import streamlit as st
import pypdf
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings


loader = PyPDFLoader("data/E24AlcaldiaBog2019.pdf")
pages = loader.load_and_split()


api_key1 = st.secrets["OPENAI_API_KEY"]


faiss_index = FAISS.from_documents(pages, OpenAIEmbeddings())
docs = faiss_index.similarity_search("How will the community be engaged?", k=2)
for doc in docs:
    st.text((str(doc.metadata["page"]) + ":", doc.page_content[:300]))
