# 📈 Comparative Financial Analysis Dashboard

An AI-powered financial intelligence platform that combines SEC financial data, comparative analytics, and Retrieval-Augmented Generation (RAG) to analyze public companies.

## 🚀 Live Demo

**Deployed Application:** https://comparative-financial-analysis-dashboard.streamlit.app/
---

## 📌 Project Overview

This project analyzes financial performance across major semiconductor companies using SEC financial filings and SEC Company Facts data.

The solution combines:

* Financial analytics dashboard
* Revenue trend analysis
* Growth analysis
* Asset comparison
* Automated insights generation
* Retrieval-Augmented Generation (RAG)
* Citation-based financial question answering

Companies analyzed:

* NVIDIA (NVDA)
* AMD
* Intel (INTC)

---

## 🎯 Features

### Financial Analytics

* Revenue trend analysis
* Revenue growth analysis
* Asset comparison analysis
* Financial summary tables
* Executive dashboard insights

### AI-Powered Analysis

* Retrieval-Augmented Generation (RAG)
* SEC filing retrieval
* Source-grounded responses
* Hallucination mitigation
* GPT-powered financial Q&A

### Interactive Dashboard

* Streamlit web application
* Company filtering
* Interactive visualizations
* Financial KPI tracking

---

## 🏗️ System Architecture

### Financial Analytics Pipeline

SEC Company Facts API

↓

Financial Dataset Builder

↓

financial_full.csv

↓

Streamlit Dashboard

↓

Revenue Analytics

Growth Analytics

Asset Analytics

Executive Insights

---

### RAG Pipeline

SEC EDGAR Filings

↓

Document Cleaning

↓

Chunking

↓

Embeddings

↓

FAISS Vector Database

↓

Retriever

↓

GPT-4o-mini

↓

Answer + Citations

---

## 📂 Data Sources

### SEC Company Facts API

Used to collect:

* Revenue
* Assets
* Financial metrics

### SEC EDGAR Filings (10-K)

Used for:

* Risk analysis
* Strategic analysis
* AI initiative extraction
* RAG-based question answering

---

## 🛠️ Technology Stack

### Backend

* Python
* Pandas
* NumPy

### Visualization

* Streamlit
* Plotly

### AI & RAG

* LangChain
* OpenAI GPT-4o-mini
* FAISS
* HuggingFace Embeddings
* Sentence Transformers

### Data Collection

* SEC Company Facts API
* SEC EDGAR Downloader

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/RohithVarmaSuraparaju/comparative-financial-analysis-dashboard.git

cd comparative-financial-analysis-dashboard
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a .env file:

```env
OPENAI_API_KEY=your_api_key
```

---

## ▶️ Run Dashboard

```bash
streamlit run app.py
```

---

## 🤖 Run RAG Chatbot Locally

```bash
python rag/chatbot.py
```

Example Questions:

* How did Intel revenue change in 2024?
* What AI opportunities did AMD discuss?
* What risks did NVIDIA identify?
* Compare AMD and Intel business strategies.

---

## 📈 Evaluation Results

### Test Set

Questions Evaluated: 5

### Results

* Accuracy: 90%
* Citation Coverage: 100%
* Hallucination Rate: 0%

### Key Observation

The RAG system successfully retrieved relevant SEC filing sections and generated grounded responses while refusing unsupported answers when evidence was insufficient.

---

## 📌 Deployment Note

The deployed Streamlit application demonstrates the complete financial analytics dashboard.

The full RAG chatbot functionality is available in the local development environment.

The FAISS vector database was excluded from cloud deployment due to storage constraints associated with SEC filing embeddings and vector indexes.

Local Version Includes:

* SEC filing retrieval
* FAISS vector search
* GPT-powered question answering
* Source citations
* Hallucination mitigation

---

## 🔮 Future Improvements

* Financial ratio analysis
* Debt and leverage metrics
* Cash flow analysis
* Improved retrieval ranking
* Cross-document reasoning
* Multi-company comparative analysis
* Cloud-hosted vector database
* Production-grade RAG deployment

---

## 👨‍💻 Author

Rohith Varma Suraparaju
---

## 📄 License

This project was developed for educational and technical assessment purposes.

DASHBOARD SCREENSHOTS : 
<img width="1470" height="800" alt="Screenshot 2026-06-06 at 2 46 57 AM" src="https://github.com/user-attachments/assets/d8793987-a45f-4e2f-9e7e-af8520a39dcd" />
<img width="1470" height="803" alt="Screenshot 2026-06-06 at 2 46 01 AM" src="https://github.com/user-attachments/assets/19325c96-51b1-4151-a5c0-f466ab677b29" />
<img width="1470" height="797" alt="Screenshot 2026-06-06 at 2 46 42 AM" src="https://github.com/user-attachments/assets/639cc228-5048-4da5-9abf-99261d47cd6d" />
<img width="1470" height="794" alt="Screenshot 2026-06-06 at 2 47 17 AM" src="https://github.com/user-attachments/assets/715c20ac-fd15-438d-ab5e-d70d9e4699c4" />
<img width="1470" height="800" alt="Screenshot 2026-06-06 at 2 46 23 AM" src="https://github.com/user-attachments/assets/ffa0af14-3e13-4524-93f4-bad0ba7712ff" />
