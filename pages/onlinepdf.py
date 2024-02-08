import streamlit as st
from langchain.document_loaders import OnlinePDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain

loader = OnlinePDFLoader("https://www.colegioemaus.edu.ar/assets/tragedias_shakespeare.pdf")
document = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1024, chunk_overlap=64)

documents = text_splitter.split_documents(document)

embeddings = HuggingFaceEmbeddings()

vectorstore = Chroma.from_documents(documents, embeddings)

qa = ConversationalRetrievalChain.from_llm(
  llm,
  vectorstore.as_retriever(),
  return_source_documents=True
)

chat_history = []

query = "Which is the author and how many books appear?"

result = qa({"question": query, "chat_history": chat_history})

st.write(result["answer"])
