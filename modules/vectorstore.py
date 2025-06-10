from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from modules.pdfhandler import save_files
from langchain.vectorstores import Chroma
from langchain.document_loaders import PyPDFLoader

import os
PERSIST_DIR="./chroma_store"
def load_vectorstore(uploaded_files):
    paths=save_files(uploaded_files)
    docs=[]
    for path in paths:
        loader=PyPDFLoader(path)
        docs.extend(loader.load())
        splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
        texts=splitter.split_documents(docs)
        embeddings=HuggingFaceEmbeddings(model_name="all-MiniLM-L12-v2")
        
        if os.path.exists(PERSIST_DIR) and os.listdir(PERSIST_DIR):
        # Append to existing
            vectorstore = Chroma(persist_directory=PERSIST_DIR, embedding_function=embeddings)
            vectorstore.add_documents(texts)
            vectorstore.persist()
        else:
        # Create new
            vectorstore = Chroma.from_documents(
            documents=texts,
            embedding=embeddings,
            persist_directory=PERSIST_DIR
        )
        vectorstore.persist()

    return vectorstore
