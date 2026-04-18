from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import FakeEmbeddings
from langchain_core.documents import Document

docs = [
    Document(page_content="RAG stands for Retrieval Augmented Generation"),
    Document(page_content="LangGraph enables multi-agent orchestration"),
]

db = FAISS.from_documents(docs, FakeEmbeddings(size=1536))
retriever = db.as_retriever()

def get_context(query):
    results = retriever.invoke(query)
    return " ".join([r.page_content for r in results])