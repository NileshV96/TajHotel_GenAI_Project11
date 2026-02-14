from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os

from app.retrieval.retriever import retrieve_similar_chunks

load_dotenv()

app = FastAPI()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class ChatRequest(BaseModel):
    question: str


@app.post("/chat")
def chat(request: ChatRequest):

    # 1. Retrieve context
    context_chunks = retrieve_similar_chunks(request.question)

    context = "\n\n".join(context_chunks)

    # 2. Build prompt
    prompt = f"""
    You are a hotel assistant chatbot.
    Use the provided context to answer the question.

    Context:
    {context}

    Question:
    {request.question}
    """

    # 3. Generate answer
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful hotel assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return {
        "answer": response.choices[0].message.content
    }
