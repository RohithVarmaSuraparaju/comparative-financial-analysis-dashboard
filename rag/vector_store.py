from pathlib import Path
import re

from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


def clean_text(text):
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text


def load_filings():

    docs = []

    filing_paths = list(
        Path("data/sec-edgar-filings").rglob(
            "full-submission.txt"
        )
    )

    for path in filing_paths:

        with open(
            path,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as f:
            text = f.read()

        docs.append(
            Document(
                page_content=clean_text(text),
                metadata={
                    "source": str(path)
                }
            )
        )

    return docs


def build_vector_store():

    docs = load_filings()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=3000,
        chunk_overlap=300
    )

    chunks = splitter.split_documents(docs)

    print(f"Chunks: {len(chunks)}")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.from_documents(
        chunks,
        embeddings
    )

    db.save_local("faiss_index")

    print("FAISS database saved.")


if __name__ == "__main__":
    build_vector_store()