# Medical Research Assistant using Retrieval-Augmented Generation (RAG)

## Overview

The Medical Research Assistant is an AI-powered application that answers medical research questions using Retrieval-Augmented Generation (RAG). Instead of relying only on the knowledge of a Large Language Model (LLM), the system retrieves relevant information from medical research papers and generates accurate, evidence-based responses with source citations.

The current implementation focuses on Alzheimer's disease research and allows users to ask questions in natural language through a Streamlit web interface.

---

## Features

- Retrieval-Augmented Generation (RAG) pipeline
- Semantic search using FAISS vector database
- PDF document loading and preprocessing
- Intelligent document chunking
- Hugging Face sentence embeddings
- Groq Llama 3.1 LLM integration
- Source citation with document title and page number
- Streamlit-based chatbot interface
- Modular project structure for easy customization

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| Programming Language | Python |
| Framework | LangChain |
| Embedding Model | BAAI/bge-base-en-v1.5 |
| Vector Database | FAISS |
| Large Language Model | Llama 3.1 8B Instant (Groq) |
| User Interface | Streamlit |
| PDF Processing | PyMuPDF |
| Environment Management | Conda |

---

## Project Structure

```text
Medical_Research_Assistant/
│
├── app.py
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
│
├── data/
│   └── papers/
│       └── .gitkeep
│
├── src/
│   ├── __init__.py
│   ├── pdf_loader.py
│   ├── text_splitter.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── llm.py
│   ├── prompts.py
│   └── rag_pipeline.py
│
└── vector_db/
    ├── index.faiss
    └── index.pkl
```

---

## System Architecture

```text
Medical Research Papers (PDFs)
            │
            ▼
        PDF Loader
            │
            ▼
     Text Splitter
            │
            ▼
 Hugging Face Embeddings
            │
            ▼
     FAISS Vector Store
            │
            ▼
      Document Retriever
            │
            ▼
      Groq Llama 3.1
            │
            ▼
 Answer with Source Citations
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/nivedhavenkatesan2005-09/Medical-Research-Assistant.git

cd Medical-Research-Assistant
```

---

### Create a Conda Environment

```bash
conda create -n medrag python=3.11

conda activate medrag
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key_here
```

Do **not** commit your `.env` file to GitHub.

---

## Add Research Papers

Place your medical research papers (PDF format) inside:

```text
data/papers/
```

> **Note:** Research papers are not included in this repository due to copyright restrictions.

---

## Build the Vector Database

Run the following command:

```bash
python src/vector_store.py
```

This creates:

```text
vector_db/
├── index.faiss
└── index.pkl
```

---

## Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your default web browser.

---

## Example Questions

- What is Alzheimer's disease?
- What biomarkers are used to diagnose Alzheimer's disease?
- What are the symptoms of Alzheimer's disease?
- Explain the role of APOE ε4 in Alzheimer's disease.
- How does MRI help diagnose Alzheimer's disease?
- What imaging techniques are used for Alzheimer's diagnosis?
- What are cerebrospinal fluid biomarkers?
- Explain amyloid-beta and tau proteins.

---

## Sample Output

**Question**

```
What biomarkers are used to diagnose Alzheimer's disease?
```

**Answer**

```
Common biomarkers include amyloid-beta (Aβ), total tau (t-tau),
phosphorylated tau (p-tau), neurofilament light chain (NfL),
blood biomarkers, cerebrospinal fluid biomarkers,
and neuroimaging biomarkers such as MRI and PET.
```

**Sources**

```
Biofluid Biomarkers in Alzheimer's Disease (Page 8)

Imaging Techniques in Alzheimer's Disease (Page 2)

Neuroimaging Biomarkers in Alzheimer's Disease (Page 1)
```

---

## Future Improvements

- Upload PDF documents directly from the Streamlit interface
- Multi-document comparison
- Multi-disease support
- Citation highlighting
- Conversation history
- Export chat as PDF
- Voice-based interaction
- Cloud deployment

---

## Author

**Nivedha V**

Bachelor of Engineering in Computer Science and Engineering

Areas of Interest:

- Artificial Intelligence
- Machine Learning
- Deep Learning
- Natural Language Processing
- Large Language Models
- Retrieval-Augmented Generation (RAG)

---

## License

This project is licensed under the MIT License.

---

## Acknowledgements

This project was developed using the following open-source technologies:

- LangChain
- Hugging Face
- FAISS
- Streamlit
- Groq
- PyMuPDF
- Sentence Transformers

---

## Disclaimer

This application is intended for educational and research purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment.
