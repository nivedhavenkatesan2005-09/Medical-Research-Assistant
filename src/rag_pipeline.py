import os

from retriever import load_vector_store
from llm import get_llm
from prompts import SYSTEM_PROMPT


# ---------------------------------------------------------
# Remove unwanted chunks
# ---------------------------------------------------------

def clean_documents(documents):

    filtered = []

    ignore_words = [
        "references",
        "bibliography",
        "acknowledgement",
        "acknowledgment",
        "doi.org"
    ]

    for doc in documents:

        text = doc.page_content.lower()

        if any(word in text for word in ignore_words):
            continue

        filtered.append(doc)

    return filtered


# ---------------------------------------------------------
# Build Context
# ---------------------------------------------------------

def build_context(documents):

    context = ""

    for i, doc in enumerate(documents, start=1):

        title = doc.metadata.get("title")

        if not title or title.strip() == "":
            title = os.path.splitext(
                os.path.basename(doc.metadata["source"])
            )[0]

        page = doc.metadata.get("page", 0) + 1

        context += f"""
Document {i}

Title:
{title}

Page:
{page}

Content:
{doc.page_content}

-------------------------------------------------------
"""

    return context


# ---------------------------------------------------------
# Extract Sources
# ---------------------------------------------------------

def get_sources(documents):

    sources = []

    seen = set()

    for doc in documents:

        title = doc.metadata.get("title")

        if not title or title.strip() == "":
            title = os.path.splitext(
                os.path.basename(doc.metadata["source"])
            )[0]

        page = doc.metadata.get("page", 0) + 1

        key = (title, page)

        if key not in seen:
            seen.add(key)
            sources.append({
                "title": title,
                "page": page
            })

    return sources


# ---------------------------------------------------------
# Initialize only once
# ---------------------------------------------------------

print("Loading Vector Database...")

vector_store = load_vector_store()

retriever = vector_store.as_retriever(

    search_type="mmr",

    search_kwargs={
        "k": 8,
        "fetch_k": 25
    }

)

print("Loading LLM...")

llm = get_llm()

print("System Ready!")


# ---------------------------------------------------------
# Main RAG Function
# ---------------------------------------------------------

def answer_question(question):

    docs = retriever.invoke(question)

    docs = clean_documents(docs)

    context = build_context(docs)

    prompt = f"""
{SYSTEM_PROMPT}

Research Context:

{context}

Question:

{question}

Answer:
"""

    response = llm.invoke(prompt)

    sources = get_sources(docs)

    return {
        "answer": response.content,
        "sources": sources,
        "documents": docs
    }


# ---------------------------------------------------------
# Terminal Mode
# ---------------------------------------------------------

def main():

    print("=" * 70)
    print("🧠 Medical Research Assistant")
    print("Type 'exit' to quit.")
    print("=" * 70)

    while True:

        question = input("\nAsk a Question: ")

        if question.lower() == "exit":
            break

        result = answer_question(question)

        print("\n" + "=" * 70)
        print("🧠 ANSWER\n")

        print(result["answer"])

        print("\n📚 SOURCES\n")

        for source in result["sources"]:

            print(
                f"📄 {source['title']} (Page {source['page']})"
            )

        print("=" * 70)


if __name__ == "__main__":
    main()