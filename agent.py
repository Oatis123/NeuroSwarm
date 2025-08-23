from agents.queen import request_to_queen
from langchain_core.messages import SystemMessage, HumanMessage


def request_to_agent(request: str)->str:
    messages = {"messages": [HumanMessage(request)]}
    return request_to_queen(messages)["messages"][-1].content


def request_to_agent_with_chat_history(chat_history: list)->str:
    messages = {"messages": chat_history}
    return request_to_queen(messages)["messages"][-1].content