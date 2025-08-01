import os
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA


def get_llm_chain(vectorstore):
    groq_key = os.environ.get("GROQ_API_KEY")
    if not groq_key:
        raise ValueError("GROQ_API_KEY not set in environment")
    llm = ChatGroq(
        groq_api_key=groq_key,
        model_name="llama3-8b-8192"
    )
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
    )