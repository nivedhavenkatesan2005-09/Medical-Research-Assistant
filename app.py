
import streamlit as st
import sys
import os

sys.path.append(
    os.path.join(os.path.dirname(__file__), "src")
)

st.set_page_config(
    page_title="Medical Research Assistant",
    page_icon="🩺",
    layout="wide"
)

with st.sidebar:
    st.title("🩺 Medical Research Assistant")
    st.markdown("---")

    st.write("### About")
    st.write(
        "Ask questions about Alzheimer's disease "
        "using information retrieved from medical "
        "research papers."
    )

    st.markdown("---")

    st.write("**Technology Stack**")
    st.write("• LangChain")
    st.write("• FAISS")
    st.write("• Hugging Face Embeddings")
    st.write("• Groq Llama 3.1")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

st.title("🩺 Medical Research Assistant")
st.caption(
    "Ask questions based on your indexed "
    "Alzheimer's disease research papers."
)

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message.get("sources"):
            with st.expander("📚 View Sources"):
                for source in message["sources"]:
                    st.write(
                        f"📄 {source['title']} "
                        f"(Page {source['page']})"
                    )

# Accept a new question
question = st.chat_input("Ask your medical research question...")

if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        try:
            with st.spinner(
                "Searching research papers and generating an answer..."
            ):
                from rag_pipeline import answer_question

                result = answer_question(question)

            answer = result["answer"]
            sources = result["sources"]

            st.markdown(answer)

            if sources:
                with st.expander("📚 View Sources"):
                    for source in sources:
                        st.write(
                            f"📄 {source['title']} "
                            f"(Page {source['page']})"
                        )
            else:
                st.info("No source details were returned.")

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer,
                "sources": sources
            })

        except Exception as e:
            st.error(
                "Unable to generate an answer. "
                "Please check your vector database, "
                "API configuration, and terminal error."
            )
            st.exception(e)
