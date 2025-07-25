import streamlit as st
from dotenv import load_dotenv

def main():
  load_dotenv()
  st.set_page_config(page_title="Chat with multiple PDFs",page_icon=":books:")

  st.header("Chat with multiple PDFs :books:")
  st.text_input("Ask a question about your document:")

  with st.sidebar:
    st.subheader("Your Documents")
    st.file_uploader("Upload your PDFs here and click on 'process'")
    st.button("process")

