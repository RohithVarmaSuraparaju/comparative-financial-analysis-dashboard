from dotenv import load_dotenv

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_openai import ChatOpenAI

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = db.as_retriever(
    search_kwargs={"k": 3}
)

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

print("\nFinancial RAG Chatbot Ready")
print("Type exit to quit\n")

while True:

    question = input("Question: ")

    if question.lower() == "exit":
        break

    docs = retriever.get_relevant_documents(
        question
    )

    context = "\n\n".join(
        [doc.page_content[:3000] for doc in docs]
    )

    prompt = f"""
You are a financial analyst.

Answer ONLY using the provided context.

If the answer is not present, say:
'I could not find sufficient evidence in the filings.'

Question:
{question}

Context:
{context}
"""

    response = llm.invoke(prompt)

    print("\nANSWER\n")
    print(response.content)

    print("\nSOURCES\n")

    for doc in docs:

        print(
            doc.metadata["source"]
        )

    print("\n--------------------\n")