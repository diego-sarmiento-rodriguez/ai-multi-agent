from langchain_community.embeddings import FakeEmbeddings
import numpy as np

# Simulamos embeddings (en producción usarías reales)
embeddings = FakeEmbeddings(size=1536)

# Definimos "intenciones"
INTENTS = {
    "rag_agent": "questions that require external knowledge or context",
    "general_agent": "general questions, conversations or creative tasks"
}

# Pre-calcular embeddings de intenciones
intent_vectors = {
    key: embeddings.embed_query(value)
    for key, value in INTENTS.items()
}


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def route_decision(state):
    query = state["input"]

    query_vec = embeddings.embed_query(query)

    scores = {
        intent: cosine_similarity(query_vec, vec)
        for intent, vec in intent_vectors.items()
    }

    best_match = max(scores, key=scores.get)

    print(f"[ROUTER] Scores: {scores} → Selected: {best_match}")

    return best_match