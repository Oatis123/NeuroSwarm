from langchain_core.tools import tool
from agents.worker import worker
import threading
from rich.progress import track

@tool
def request_to_swarm(tasks: list[str])->str:
    """Функция для выдачи задач агентам работникам, принимает на вход список задач (максимум 15) в 
    формате строк и возвращает список ответов в формате строки: Ответ на задачу1: ответ\n Ответ на зхадчу 2: Ответ"""
    agent_count = 0
    threads = []
    answers = []
    for task in tasks: 
        agent_count += 1
        thread = threading.Thread(target=worker, args=(task, answers))
        threads.append(thread)
        thread.start()
    description = f"[green]{agent_count} {'agent' if agent_count == 1 else 'agents'} working on the task\n"
    for thr in track(threads, description=description):
        thr.join()
    return "\n".join(answers)