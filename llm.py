from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_available_model():
    models = client.models.list()
    
    # Filtra modelos tipo chat/completions
    for m in models.data:
        if "chat" in m.id or "llama" in m.id or "mixtral" in m.id:
            return m.id
    
    # fallback si algo raro pasa
    return models.data[0].id


MODEL_NAME = get_available_model()
print(f"[INFO] Using model: {MODEL_NAME}")


def call_llm(prompt):
    print(f"[LLM CALL] Model: {MODEL_NAME} | Prompt length: {len(prompt)}")

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content