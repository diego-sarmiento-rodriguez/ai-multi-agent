from fastapi import FastAPI
from graph import app_graph
from fastapi import Response

api = FastAPI()

@api.get("/")
def root():
    return {"message": "Multi-agent API running 🚀"}


@api.get("/ask")
def ask(q: str):
    result = app_graph.invoke({"input": q})

    return {
        "question": q,
        "response": result.get("output"),
        "agent_used": result.get("agent")
    }

@api.get("/favicon.ico")
def favicon():
    return Response(status_code=204)


@api.get("/ask")
def ask(q: str, session_id: str = "default"):
    result = app_graph.invoke({
        "input": q,
        "session_id": session_id  # 👈 CLAVE
    })

    return {
        "question": q,
        "response": result.get("output"),
        "agent_used": result.get("agent"),
        "session_id": session_id
    }