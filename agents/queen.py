from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_cohere import ChatCohere
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.prebuilt import create_react_agent
from prompts.queen_prompt import prompt
from tools.queen_tools import request_to_swarm
import os
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", api_key=api_key, temperature=0.5)

tools = [request_to_swarm]

queen_agent = create_react_agent(
    model=llm,
    tools=tools
)


system_prompt = prompt

def request_to_queen(request: str)->str:
    req = {"messages": [SystemMessage(system_prompt), HumanMessage(request)]}
    response = queen_agent.invoke(input=req)
    return response["messages"][-1].content
