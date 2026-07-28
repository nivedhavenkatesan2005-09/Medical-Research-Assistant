import os

from langchain_community.vectorstores import FAISS
from embeddings import get_embedding_model


def load_vector_store():

    embeddings = get_embedding_model()

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(base_dir, "vector_db")

    vector_store = FAISS.load_local(
        db_path,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_store