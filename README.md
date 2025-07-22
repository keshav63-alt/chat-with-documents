# chat-with-documents
A Streamlit-based AI chatbot that allows users to upload documents (TXT, PDF, CSV) and interact with them using Google Gemini (gemini-2.5-flash-lite-preview-06-17) for question answering.  It leverages LangChain, FAISS, and Google Generative AI embeddings to retrieve context-aware responses from the uploaded files.

# Chat with Multiple Documents (Streamlit + Google Gemini)

This project is a **Streamlit-based AI chatbot** that enables users to upload documents (TXT, PDF, or CSV) and ask questions based on the content of the uploaded files.  
The chatbot uses **Google Gemini (gemini-2.5-flash-lite-preview-06-17)** as the LLM along with **FAISS** for vector search and **Google Generative AI Embeddings** for semantic understanding.

---

## 🚀 Features
- **Upload TXT, PDF, or CSV files** for processing.
- **Chunking of large documents** for better context retrieval.
- **FAISS Vector Database** for efficient search of relevant content.
- **Google Gemini LLM** for intelligent and context-aware responses.
- **Streamlit UI** for an interactive and simple user experience.

---

## 🛠 Tech Stack
- **Python 3.9+**
- **Streamlit**
- **LangChain**
- **FAISS**
- **Google Generative AI (Gemini API)**
- **dotenv** (for environment variable management)

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
2. **Create a virtual environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

3. Install dependencies

bash
Copy
Edit
pip install -r requirements.txt

4.Set up Google Gemini API Key

Create a .env file in the root directory.

Add your Google API key:

env
Copy
Edit
GOOGLE_API_KEY=your_google_gemini_api_key

5.Run the Streamlit app

bash
Copy
Edit
streamlit run app.py

📂 Project Structure
bash
Copy
Edit
.
├── app.py              # Main Streamlit application
├── requirements.txt    # Dependencies
├── .env                # API key (not committed)
└── README.md           # Project documentation
