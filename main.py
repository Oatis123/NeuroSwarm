from agents.queen import request_to_queen
from langchain_core.messages import HumanMessage, SystemMessage
from prompts.queen_prompt import prompt as system_prompt
from rich.console import Console
from rich.markdown import Markdown
from components import neuro_swarm_art as nsa
from components import commands, models, help
from pathlib import Path
import json


if __name__ == "__main__":

    console = Console()

    Path("config.json").touch()

    configurated = True

    with open("config.json", "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except:
            configurated = False

    if configurated:

        chat_history = {"messages": [SystemMessage(system_prompt)]}
    
        console.print(nsa)
        console.print("[green]/help for commands list[/green]\n")

        console.print("\n[green]User: [/green]", end="")
        user_input = input()
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
                elif user_input == "/models":
                    models()
                else:
                    help()
            console.print("\n[green]User: [/green]", end="")
            user_input = input()
    else:
        console.print("[green]Enter your Gemini API key: [/green]", end="")
        gemini_api_key = input()
        console.print("[green]Enter your Tavily API key: [/green]", end="")
        tavily_api_key = input()
        with open("config.json", "w", encoding="utf-8") as f:
            json.dump({"gemini_api_key": gemini_api_key, "tavily_api_key": tavily_api_key}, f)
        console.print("[green]Please restart the application: [/green]", end="")