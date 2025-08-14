from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.prebuilt import create_react_agent
from prompts.worker_prompt import prompt
import os
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", api_key=api_key, temperature=0.5)


tools = []


worker_agent = create_react_agent(
    model=llm,
    tools=tools
)

system_prompt = prompt


def worker(task: str, answers_list: list):

    request = {"messages": [SystemMessage(prompt), HumanMessage(task)]}

    response = worker_agent.invoke(input=request)

    answers_list.append(f"Ответ на задачу \"{task}\": {response['messages'][-1].content}")