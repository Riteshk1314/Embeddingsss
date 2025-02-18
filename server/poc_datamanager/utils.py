from langchain.embeddings import HuggingFaceBgeEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
import os

def process_pdf(pdf_path):
    model_name = "BAAI/bge-large-en"   # "BAAI/bge-large-en" is the model name for the large model can also use small but gives error with large pdfs
    model_kwargs = {"device": "cpu"}
    encode_kwargs = {"normalize_embeddings": True}
    bln = HuggingFaceBgeEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )
    embeddings = bln

    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    print("pdf loaded now processing")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=250)# iska trial and error se pata chalega
    final_documents = text_splitter.split_documents(docs)

    persist_directory = "vector_db"
    os.makedirs(persist_directory, exist_ok=True)

    vectors = Chroma.from_documents(
        documents=final_documents,
        embedding=embeddings,
        persist_directory=persist_directory# this is the directory where the vectors db will be stored
    )
