import streamlit as st
import pypdf
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
import pickle
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
import os

loader = PyPDFLoader("data/E24AlcaldiaBog2019.pdf")
pages = loader.load_and_split()


api_key1 = st.secrets["OPENAI_API_KEY"]


st.header("Chat with pdf")

# upload a pdf file
pdf = st.file_uploader("Upload your PDF", type='pdf')

#st.write(pdf)
if pdf is not None:
    #pdf reader
    pdf_reader = PdfReader(pdf)
    
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
        )
    chunks = text_splitter.split_text(text=text)

    # # embeddings
    store_name = pdf.name[:-4]
    st.write(f'{store_name}')
    # st.write(chunks)

    if os.path.exists(f"{store_name}.pkl"):
        with open(f"{store_name}.pkl", "rb") as f:
            VectorStore = pickle.load(f)
        # st.write('Embeddings Loaded from the Disk')s
    else:
        embeddings = OpenAIEmbeddings()
        VectorStore = FAISS.from_texts(chunks, embedding=embeddings)
        with open(f"{store_name}.pkl", "rb") as f:
            pickle.dump(VectorStore, f)

    # embeddings = OpenAIEmbeddings()
    # VectorStore = FAISS.from_texts(chunks, embedding=embeddings)

    # Accept user questions/query
    query = st.text_input("Ask questions about your PDF file:")
    # st.write(query)

    if query:
        docs = VectorStore.similarity_search(query=query, k=3)

        llm = OpenAI()
        chain = load_qa_chain(llm=llm, chain_type="stuff")
        with get_openai_callback() as cb:
            response = chain.run(input_documents=docs, question=query)
            print(cb)
        st.write(response)
