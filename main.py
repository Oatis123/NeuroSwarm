from agents.queen import request_to_queen
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, ToolMessage
from rich.console import Console
from rich.markdown import Markdown

console = Console()

resp = request_to_queen("""
Напиши две простых прогаммы для вывода Hello World в консоль на kotlin и python
""")

#Для дебага
#for i in resp:
#    if isinstance(i, AIMessage):
#        print("\n--------------------AIMessage--------------------\n")
#        if i.content == "":
#            print(i.additional_kwargs)
#        else:
#            for chunk in i.content:
#                console.print(Markdown(chunk))
#        print("\n--------------------AIMessage--------------------\n\n")
#    elif isinstance(i, SystemMessage):
#        print("\n--------------------SystemMessage--------------------\n")
#        print(i.content)
#        print("\n--------------------SystemMessage--------------------\n\n")
#    elif isinstance(i, ToolMessage):
#        print("\n--------------------ToolMessage--------------------\n")
#        print(i.content)
#        print("\n--------------------ToolMessage--------------------\n\n")
#    else:
#        print("\n--------------------HumanMessage--------------------\n")
#        print(i.content)
#        print("\n--------------------HumanMessage--------------------\n\n")

print("\n\n\n")
for chunk in resp:
    console.print(Markdown(chunk))