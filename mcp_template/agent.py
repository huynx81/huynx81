"""Minimal agent that uses the OllamaTool."""

from dataclasses import dataclass
from .tool import OllamaTool


@dataclass
class Agent:
    """Simple agent that delegates to an OllamaTool."""

    tool: OllamaTool

    def handle(self, prompt: str, model: str = "llama2") -> str:
        """Process a user prompt and return the tool's response."""
        return self.tool.chat(prompt=prompt, model=model)
