from agents.queen import request_to_queen
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, ToolMessage
from prompts.queen_prompt import prompt as system_prompt
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from components import neuro_swarm_art as nsa

console = Console()

chat_history = {"messages": [SystemMessage(system_prompt)]}

console.print(nsa)
console.print("[green]/help for commands list[/green]\n")

console.print("\n[green]User: [/green]", end="")
user_input = input()
commands = ["/help", "/stop"]

while True:
    if user_input not in commands:

        chat_history["messages"].append(HumanMessage(user_input))

        console.print("\n[green]NeuroSwarm: [/green]\n")

        resp = request_to_queen(chat_history)
        chat_history = resp

        if isinstance(resp["messages"][-1].content, list):
            for chunk in resp:
                console.print(Markdown(chunk))
        else:
            console.print(Markdown(resp["messages"][-1].content))
    else:
        if user_input == "/stop":
            break
        else:
            console.print("\n[green]System: [/green]")

            command_text = "\n".join(f"  • {cmd}" for cmd in commands)
            console.print(
                Panel(
                    command_text,
                    title="[bold cyan]Available Commands[/bold cyan]",
                    border_style="green",
                    expand=False
                )
            )
            
    console.print("\n[green]User: [/green]", end="")
    user_input = input()