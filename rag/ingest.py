from pathlib import Path
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
import re


def clean_text(text):

    # remove excessive whitespace
    text = re.sub(r"\s+", " ", text)

    # remove xml/html tags
    text = re.sub(r"<[^>]+>", " ", text)

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

        text = clean_text(text)

        docs.append(
            Document(
                page_content=text,
                metadata={
                    "source": str(path)
                }
            )
        )

    return docs


def chunk_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=3000,
        chunk_overlap=300
    )

    return splitter.split_documents(documents)


if __name__ == "__main__":

    docs = load_filings()

    chunks = chunk_documents(docs)

    print(f"Loaded {len(docs)} documents")
    print(f"Created {len(chunks)} chunks")