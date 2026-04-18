from langgraph.graph import StateGraph

from agents import general_agent, rag_agent
from router import route_decision


def run_general(state):
    session_id = state.get("session_id", "default")  # 👈 seguro
    response = rag_agent(state["input"], session_id)

    return {
        "output": response,
        "agent": "rag_agent"
    }



def run_rag(state):
    session_id = state.get("session_id", "default")  # 👈 seguro
    response = rag_agent(state["input"], session_id)

    return {
        "output": response,
        "agent": "rag_agent"
    }


graph = StateGraph(dict)

graph.add_node("general_agent", run_general)
graph.add_node("rag_agent", run_rag)

# 👇 IMPORTANTE: usar START implícito correctamente

graph.add_conditional_edges(
    "__start__",
    route_decision,
    {
        "general_agent": "general_agent",
        "rag_agent": "rag_agent",
    },
)


# 👇 FINES CLAROS (no paralelos)
graph.set_finish_point("general_agent")
graph.set_finish_point("rag_agent")

app_graph = graph.compile()