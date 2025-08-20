from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from prompts.simple_worker_prompt import prompt
from utils import gemini_api_key


api_key = gemini_api_key

llm = ChatGoogleGenerativeAI(model="gemma-3-27b-it", api_key=api_key, temperature=0.5)

system_prompt = prompt

def worker(task: str, answers_list: list):

    request = [HumanMessage(system_prompt + "\n" + task)]

    response = llm.invoke(input=request)

    answers_list.append(f"Ответ на задачу \"{task}\": {response.content}")