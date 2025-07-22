import streamlit as st
from Rag_pipeline import answer_query,load_document,create_vector_db

# -------------------------
# Streamlit UI
# -------------------------
st.set_page_config(page_title="Chat with Documents", layout="wide")
st.title("📄 Chat with Multiple Documents")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

uploaded_file = st.file_uploader("Upload a TXT, PDF, or CSV file", type=["txt", "pdf", "csv"])
user_query = st.text_input("Enter your question")

if uploaded_file:
    docs = load_document(uploaded_file)
    if docs:
        st.success("Document loaded successfully!")
        vector_db = create_vector_db(docs)

        if st.button("Get Answer"):
            with st.spinner("Thinking..."):
                answer = answer_query(vector_db, user_query)
                st.session_state.chat_history.append((user_query, answer))

# Display chat history
if st.session_state.chat_history:
    st.subheader("Chat History")
    for q, a in st.session_state.chat_history:
        st.markdown(f"**Q:** {q}")
        st.markdown(f"**A:** {a}")
        st.markdown("---")
