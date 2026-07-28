from pdf_loader import load_documents
from text_splitter import split_documents

documents = load_documents("data/papers")
chunks = split_documents(documents)

print(f"Total Pages: {len(documents)}")
print(f"Total Chunks: {len(chunks)}")

print("\nFirst Chunk:\n")
print(chunks[0].page_content[:500])

print("\nMetadata:\n")
print(chunks[0].metadata)