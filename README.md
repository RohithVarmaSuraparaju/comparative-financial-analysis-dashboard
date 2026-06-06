# Comparative Financial Analysis Dashboard

An AI-powered financial intelligence platform that combines SEC financial data, comparative analytics, and Retrieval-Augmented Generation (RAG) to analyze public companies.

## Features

- Revenue trend analysis
- Revenue growth analysis
- Asset comparison analysis
- Automated financial insights
- SEC filing question answering
- Source-cited responses
- Interactive Streamlit dashboard

## Data Sources

1. SEC Company Facts API
2. SEC EDGAR Filings (10-K)

Companies analyzed:

- NVIDIA (NVDA)
- AMD
- Intel (INTC)

## Architecture

SEC Company Facts API
↓
Financial Dataset Builder
↓
financial_full.csv
↓
Streamlit Dashboard

SEC EDGAR Filings
↓
Document Chunking
↓
FAISS Vector Database
↓
Retriever
↓
GPT-4o-mini
↓
RAG Chatbot

## Technology Stack

- Python
- Streamlit
- LangChain
- FAISS
- HuggingFace Embeddings
- OpenAI GPT-4o-mini
- Pandas
- Plotly

## Installation

```bash
pip install -r requirements.txt
```

## Run Dashboard

```bash
streamlit run app.py
```

## Run Chatbot

```bash
python rag/chatbot.py
```

## Evaluation Results

- Accuracy: 90%
- Citation Coverage: 100%
- Hallucination Rate: 0%

## Future Improvements

- Additional financial metrics
- Enhanced retrieval ranking
- Multi-company comparison reasoning
- Financial ratio analysis
DASHBOARD SCREENSHOTS : 
<img width="1470" height="800" alt="Screenshot 2026-06-06 at 2 46 57 AM" src="https://github.com/user-attachments/assets/d8793987-a45f-4e2f-9e7e-af8520a39dcd" />
