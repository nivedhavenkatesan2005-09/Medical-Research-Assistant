import streamlit as st
import sys
import os

# --------------------------------------------------
# Add src folder to Python path
# --------------------------------------------------

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from rag_pipeline import answer_question


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Medical Research Assistant",
    page_icon="🩺",
    layout="wide"
)


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.title("🩺 Medical Research Assistant")

    st.markdown("---")

    st.write("### About")

    st.write("""
This chatbot answers questions from Alzheimer's Disease research papers using:

- Research Papers
- Groq Llama 3.1
- FAISS Vector Search
- HuggingFace Embeddings
- LangChain
    """)

    st.markdown("---")

    if st.button("🗑 Clear Chat"):

        st.session_state.messages = []

        st.rerun()


# --------------------------------------------------
# Main Title
# --------------------------------------------------

st.title("🩺 Medical Research Assistant")

st.caption("Ask questions based on Alzheimer's Disease research papers.")


# --------------------------------------------------
# Chat History
# --------------------------------------------------

if "messages" not in st.session_state:

    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# --------------------------------------------------
# Chat Input
# --------------------------------------------------

question = st.chat_input(
    "Ask your medical question..."
)
