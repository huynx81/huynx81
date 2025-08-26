"""Tool for interacting with the MCP server."""

from dataclasses import dataclass
import requests


@dataclass
class OllamaTool:
    """A simple tool that communicates with the MCP server."""

    server_url: str = "http://localhost:8000"

    def chat(self, prompt: str, model: str = "llama2") -> str:
        """Send a prompt to the server and return the response."""
        payload = {"prompt": prompt, "model": model}
        resp = requests.post(f"{self.server_url}/chat", json=payload, timeout=60)
        resp.raise_for_status()
        data = resp.json()
        return data["response"]
