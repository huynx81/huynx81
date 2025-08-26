"""Simple MCP server using FastAPI and a local Ollama model.

This server exposes a `/chat` endpoint that relays user prompts to a
locally running Ollama model and returns the generated response.

Run with:
    uvicorn mcp_template.server:app --reload
"""

from fastapi import FastAPI
from pydantic import BaseModel
import ollama

app = FastAPI()


class ChatRequest(BaseModel):
    prompt: str
    model: str = "llama2"


class ChatResponse(BaseModel):
    response: str


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest) -> ChatResponse:
    """Generate a response from the local Ollama model."""
    result = ollama.chat(model=req.model, messages=[{"role": "user", "content": req.prompt}])
    message = result["message"]["content"]
    return ChatResponse(response=message)
