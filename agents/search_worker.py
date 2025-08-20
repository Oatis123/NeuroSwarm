from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.prebuilt import create_react_agent
from prompts.search_worker_prompt import prompt
from tools.web_tools import scrape_webpage, duckduckgo_search
from utils import gemini_api_key


api_key = gemini_api_key

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite", api_key=api_key, temperature=0.5)


tools = [duckduckgo_search, scrape_webpage]


worker_agent = create_react_agent(
    model=llm,
    tools=tools
)

system_prompt = prompt


def worker(task: str, answers_list: list):

    request = {"messages": [SystemMessage(prompt), HumanMessage(task)]}

    response = worker_agent.invoke(input=request)

    answers_list.append(f"Ответ на задачу \"{task}\": {response['messages'][-1].content}")