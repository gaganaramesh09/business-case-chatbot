from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Business Case Chatbot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

SYSTEM_PROMPT = """You are a sharp, experienced management consultant and financial analyst. You help users analyze business cases with rigor and clarity.

When a user presents a business scenario:
1. Identify the core business question
2. Apply relevant frameworks and mention which you are using
3. Structure your answer with clear sections
4. For financial analyses, show key calculations and assumptions
5. Flag risks and sensitivities
6. End with a clear recommendation

Keep responses focused and actionable. Use plain language. Format with markdown where helpful."""


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]


class ChatResponse(BaseModel):
    reply: str


@app.get("/")
def root():
    return {"status": "Business Case Chatbot API is running"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    messages = [{"role": m.role, "content": m.content} for m in request.messages]
    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=messages,
    )
    reply = response.content[0].text
    return ChatResponse(reply=reply)
