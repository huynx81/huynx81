"""Command line client for interacting with the agent."""

from .tool import OllamaTool
from .agent import Agent


def main() -> None:
    tool = OllamaTool()
    agent = Agent(tool)
    print("Type 'exit' to quit.")
    while True:
        try:
            prompt = input("You: ")
        except EOFError:
            break
        if prompt.lower() in {"exit", "quit"}:
            break
        response = agent.handle(prompt)
        print(f"Agent: {response}")


if __name__ == "__main__":
    main()
