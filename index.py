import streamlit as st
import warnings
import logging
from modules.pdfhandler import upload_files,save_files
from modules.llm import get_llm_chain
from modules.vectorstore import load_vectorstore
from modules.chat import display_chat_history, handle_user_input, download_chat_history

warnings.filterwarnings("ignore")
logging.getLogger("transformers").setLevel(logging.ERROR)

st.set_page_config(page_title="Chat with Attached Documents", page_icon=":books:")
st.header("Chat with Multiple Documents")

uploaded_files,submitted = upload_files()

if submitted and uploaded_files:
    with st.spinner("Processing..."):
        vectorstore = load_vectorstore(uploaded_files)
        st.session_state.vectorstore = vectorstore

display_chat_history()

if "vectorstore" in st.session_state:
    handle_user_input(get_llm_chain(st.session_state.vectorstore))

download_chat_history()
