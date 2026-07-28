import os
import shutil
import time

from langchain_community.vectorstores import FAISS

from pdf_loader import load_documents
from text_splitter import split_documents
from embeddings import get_embedding_model


VECTOR_DB_PATH = "vector_db"


def create_vector_store():

    start_time = time.time()

    print("=" * 70)
    print("MEDICAL RESEARCH ASSISTANT")
    print("FAISS VECTOR DATABASE CREATION")
    print("=" * 70)

    try:

        # -------------------------------------------------------
        # Load PDFs
        # -------------------------------------------------------

        print("\n📄 Loading Research Papers...")

        documents = load_documents("data/papers")

        print(f"✅ Pages Loaded : {len(documents)}")

        # -------------------------------------------------------
        # Split Documents
        # -------------------------------------------------------

        print("\n✂ Splitting Documents into Chunks...")

        chunks = split_documents(documents)

        print(f"✅ Chunks Created : {len(chunks)}")

        # -------------------------------------------------------
        # Embedding Model
        # -------------------------------------------------------

        print("\n🧠 Loading Embedding Model...")

        embeddings = get_embedding_model()

        print("✅ Embedding Model Loaded Successfully")

        # -------------------------------------------------------
        # Remove old vector database
        # -------------------------------------------------------

        if os.path.exists(VECTOR_DB_PATH):

            print("\n🗑 Removing Old Vector Database...")

            shutil.rmtree(VECTOR_DB_PATH)

        # -------------------------------------------------------
        # Create FAISS Index
        # -------------------------------------------------------

        print("\n⚡ Creating FAISS Index...")

        vector_store = FAISS.from_documents(
            documents=chunks,
            embedding=embeddings
        )

        # -------------------------------------------------------
        # Save Database
        # -------------------------------------------------------

        print("\n💾 Saving Vector Database...")

        vector_store.save_local(VECTOR_DB_PATH)

        elapsed = round(time.time() - start_time, 2)

        print("\n" + "=" * 70)
        print("✅ VECTOR DATABASE CREATED SUCCESSFULLY")
        print("=" * 70)

        print(f"📁 Location        : {VECTOR_DB_PATH}")
        print(f"📄 Total Pages     : {len(documents)}")
        print(f"🧩 Total Chunks    : {len(chunks)}")
        print(f"🧠 Embedding Model : HuggingFace")
        print(f"⏱ Time Taken      : {elapsed} seconds")

        print("=" * 70)

    except Exception as e:

        print("\n❌ ERROR OCCURRED")
        print("=" * 70)
        print(e)
        print("=" * 70)


if __name__ == "__main__":
    create_vector_store()