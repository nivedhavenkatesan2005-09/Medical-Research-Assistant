import os
import re
from langchain_community.document_loaders import PyMuPDFLoader


# Sections after which we stop reading the paper
STOP_SECTIONS = [
    "references",
    "bibliography",
]

# Pages that should be skipped
SKIP_KEYWORDS = [
    "acknowledgements",
    "acknowledgments",
    "funding",
    "conflict of interest",
    "conflicts of interest",
    "author contributions",
    "author contribution",
    "supplementary material",
    "supplementary information",
    "ethics approval",
    "ethics statement",
    "data availability",
    "availability of data",
]


def clean_text(text):
    """
    Remove unnecessary whitespace.
    """

    text = re.sub(r"\s+", " ", text)
    return text.strip()


def should_stop(text):
    """
    Stop processing the remaining pages of the PDF
    after reaching the References section.
    """

    text = text.lower()

    first_400 = text[:400]

    return any(word in first_400 for word in STOP_SECTIONS)


def should_skip(text):
    """
    Skip pages such as funding,
    acknowledgements, etc.
    """

    text = text.lower()

    if len(text.strip()) < 150:
        return True

    first_500 = text[:500]

    if any(word in first_500 for word in SKIP_KEYWORDS):
        return True

    return False


def load_documents(pdf_folder):

    documents = []

    total_pages = 0
    kept_pages = 0
    skipped_pages = 0
    stopped_papers = 0

    pdf_files = sorted(
        [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]
    )

    print("=" * 70)
    print("Loading Research Papers")
    print("=" * 70)

    for file in pdf_files:

        path = os.path.join(pdf_folder, file)

        print(f"\nLoading: {file}")

        loader = PyMuPDFLoader(path)

        pages = loader.load()

        stop = False

        for page in pages:

            if stop:
                break

            total_pages += 1

            text = clean_text(page.page_content)

            # Stop reading once References begin
            if should_stop(text):
                stop = True
                stopped_papers += 1
                print("   ↳ References detected. Remaining pages ignored.")
                continue

            # Skip unwanted pages
            if should_skip(text):
                skipped_pages += 1
                continue

            page.page_content = text

            # Use filename if title missing
            title = page.metadata.get("title", "").strip()

            if title == "":
                page.metadata["title"] = os.path.splitext(file)[0]

            page.metadata["paper_name"] = file

            kept_pages += 1

            documents.append(page)

    print("\n" + "=" * 70)
    print("PDF LOADING SUMMARY")
    print("=" * 70)
    print(f"PDF Files Loaded          : {len(pdf_files)}")
    print(f"Total Pages Scanned       : {total_pages}")
    print(f"Pages Kept               : {kept_pages}")
    print(f"Pages Skipped            : {skipped_pages}")
    print(f"Papers Stopped at References : {stopped_papers}")
    print("=" * 70)

    return documents


if __name__ == "__main__":

    pdf_folder = "data/papers"

    documents = load_documents(pdf_folder)

    print("\nFirst Document Preview\n")
    print("-" * 70)
    print(documents[0].page_content[:800])

    print("\nMetadata\n")
    print("-" * 70)
    print(documents[0].metadata)