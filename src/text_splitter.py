from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):
    """
    Split documents into smaller overlapping chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1200,
        chunk_overlap=250,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]
    )

    chunks = splitter.split_documents(documents)

    # Remove very small chunks
    filtered_chunks = []

    for chunk in chunks:

        text = chunk.page_content.strip()

        if len(text) < 300:
            continue

        filtered_chunks.append(chunk)

    print("=" * 60)
    print(f"Total Chunks Created : {len(filtered_chunks)}")
    print("=" * 60)

    return filtered_chunks


if __name__ == "__main__":

    from pdf_loader import load_documents

    documents = load_documents("data/papers")

    chunks = split_documents(documents)

    print("\nFirst Chunk:\n")
    print(chunks[0].page_content)

    print("\nMetadata:\n")
    print(chunks[0].metadata)