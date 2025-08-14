from langchain_core.tools import tool
from agents.worker import worker
import threading

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
    print(f"Задействовано {agent_count} агента/ов")
    for thr in threads:
        thr.join()
    return "\n".join(answers)