import os
import asyncio
import nest_asyncio
import streamlit as st
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader, PyPDFLoader, CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

# -------------------------
# FIX: Async Event Loop
# -------------------------
try:
    asyncio.get_running_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

nest_asyncio.apply()

# -------------------------
# Load API Key
# -------------------------
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# -------------------------
# Initialize LLM & Embeddings
# -------------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite-preview-06-17",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.5
)

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=GOOGLE_API_KEY
)

# -------------------------
# Helper Functions
# -------------------------
def load_document(uploaded_file):
    """Load TXT, PDF, or CSV file into documents."""
    file_type = uploaded_file.name.split('.')[-1]
    temp_path = f"temp.{file_type}"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.read())

    if file_type == "txt":
        return TextLoader(temp_path, encoding="utf-8").load()
    elif file_type == "pdf":
        return PyPDFLoader(temp_path).load()
    elif file_type == "csv":
        return CSVLoader(temp_path).load()
    else:
        st.error("Unsupported file format!")
        return []

def create_vector_db(docs):
    """Create FAISS vector database from documents."""
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)
    return FAISS.from_documents(chunks, embeddings)

def answer_query(vector_db, query):
    """Retrieve relevant context and query the LLM."""
    retriever = vector_db.as_retriever(search_kwargs={"k": 4})
    relevant_docs = retriever.invoke(query)
    context = "\n\n".join([doc.page_content for doc in relevant_docs])
    prompt = f"Answer the question based on the following context:\n\n{context}\n\nQuestion: {query}"
    response = llm.invoke(prompt)
    return response.content if hasattr(response, 'content') else response

