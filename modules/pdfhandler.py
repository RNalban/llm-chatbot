import streamlit as st
import tempfile

def upload_files():
    with st.sidebar:
        st.header("Upload PDF Documents")
        uploaded_files=st.file_uploader("Choose",type="pdf",accept_multiple_files=True)
        
        submit=st.button("Process")
    return uploaded_files,submit


def save_files(uploaded_files):
    file_paths=[]
    for file in uploaded_files:
        with tempfile.NamedTemporaryFile(delete=False,suffix=".pdf") as temp_file:
            temp_file.write(file.read())
            file_paths.append(temp_file.name)
    return file_paths       