from llm import call_llm
from rag import get_context
from semantic_memory import save_memory, retrieve_memory


def general_agent(query, session_id):
    #  memoria semántica
    memory_context = retrieve_memory(session_id, query)

    prompt = f"""
    Use past memory if relevant:

    Memory:
    {memory_context}

    User:
    {query}
    """

    response = call_llm(prompt)

    #  guardar en memoria semántica
    save_memory(session_id, "user", query)
    save_memory(session_id, "assistant", response)

    return response


def rag_agent(query, session_id):
    context = get_context(query)

    #  memoria semántica
    memory_context = retrieve_memory(session_id, query)

    prompt = f"""
    Use both context and memory:

    Context:
    {context}

    Memory:
    {memory_context}

    Question:
    {query}
    """

    response = call_llm(prompt)

    #  guardar memoria
    save_memory(session_id, "user", query)
    save_memory(session_id, "assistant", response)

    return response