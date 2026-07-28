from langchain_huggingface import HuggingFaceEmbeddings


def get_embedding_model():
    """
    Load the HuggingFace embedding model for semantic search.
    """

    print("=" * 60)
    print("Loading Embedding Model")
    print("=" * 60)

    embedding_model = HuggingFaceEmbeddings(

        model_name="BAAI/bge-base-en-v1.5",

        model_kwargs={
            "device": "cpu"
        },

        encode_kwargs={
            "normalize_embeddings": True
        }

    )

    print("✅ Embedding model loaded successfully.")
    print("Model : BAAI/bge-base-en-v1.5")
    print("Device: CPU")
    print("=" * 60)

    return embedding_model


if __name__ == "__main__":

    embeddings = get_embedding_model()

    sample_query = "What biomarkers are used for Alzheimer's disease diagnosis?"

    print("\nGenerating sample embedding...")

    vector = embeddings.embed_query(sample_query)

    print("\nEmbedding Statistics")
    print("=" * 60)
    print(f"Query               : {sample_query}")
    print(f"Embedding Dimension : {len(vector)}")
    print(f"First 10 Values     : {vector[:10]}")
    print("=" * 60)