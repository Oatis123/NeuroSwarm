from ast import List
from langchain_core.messages import SystemMessage
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI


from langgraph.graph.state import CompiledStateGraph


from typing import Any


from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from tools.queen_tools import request_to_search_swarm, request_to_simple_swarm
from tools.web_tools import duckduckgo_search, scrape_webpage
from prompts.queen_prompt import prompt
from utils import gemini_api_key


api_key = gemini_api_key

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", api_key=api_key, temperature=0.5)

tools = [request_to_search_swarm, request_to_simple_swarm, duckduckgo_search, scrape_webpage]

queen_agent = create_react_agent(
    model=llm,
    tools=tools
)


def request_to_queen(chat_history: dict[str, list]):
    chat_history["messages"].insert(0, SystemMessage(prompt))
    response = queen_agent.invoke(input=chat_history)
    return response
