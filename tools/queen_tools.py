from langchain_core.tools import tool
from agents.search_worker import worker as search_worker
from agents.simple_worker import worker as simple_worker
import threading
from rich.progress import track

@tool
def request_to_search_swarm(tasks: list[str])->str:
    """Функция для выдачи задач поисковым агентам, принимает на вход список задач (максимум 15) в 
    формате строк и возвращает список ответов в формате строки: Ответ на задачу1: ответ\n Ответ на зхадчу 2: Ответ"""
    agent_count = 0
    threads = []
    answers = []
    for task in tasks: 
        agent_count += 1
        thread = threading.Thread(target=search_worker, args=(task, answers))
        threads.append(thread)
        thread.start()
    description = f"[green]{agent_count} search {'agent' if agent_count == 1 else 'agents'} working on the task\n"
    for thr in track(threads, description=description):
        thr.join()
    return "\n".join(answers)


@tool
def request_to_simple_swarm(tasks: list[str])->str:
    """Функция для выдачи задач агентам работникам, принимает на вход список задач (максимум 30) в 
    формате строк и возвращает список ответов в формате строки: Ответ на задачу1: ответ\n Ответ на зхадчу 2: Ответ"""
    agent_count = 0
    threads = []
    answers = []
    for task in tasks: 
        agent_count += 1
        thread = threading.Thread(target=simple_worker, args=(task, answers))
        threads.append(thread)
        thread.start()
    description = f"[green]{agent_count} simple {'agent' if agent_count == 1 else 'agents'} working on the task\n"
    for thr in track(threads, description=description):
        thr.join()
    return "\n".join(answers)