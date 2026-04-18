from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import FakeEmbeddings
from langchain_core.documents import Document

# embeddings (demo)
embeddings = FakeEmbeddings(size=1536)

# memoria por sesión
memory_stores = {}


def get_or_create_store(session_id):
    if session_id not in memory_stores:
        dummy_doc = Document(page_content="initial memory")

        memory_stores[session_id] = FAISS.from_documents(
            [dummy_doc],  # 👈 mínimo 1 doc
            embeddings
        )
    return memory_stores[session_id]


def save_memory(session_id, role, content):
    store = get_or_create_store(session_id)

    doc = Document(
        page_content=content,
        metadata={"role": role}
    )

    store.add_documents([doc])


def retrieve_memory(session_id, query):
    store = get_or_create_store(session_id)

    results = store.similarity_search(query, k=3)

    return " ".join([
        r.page_content
        for r in results
        if r.page_content != "initial memory"
    ])