from threading import Thread
from typing import Any
from langchain_core.tools import tool
from agents.search_worker import worker as search_worker
from agents.simple_worker import worker as simple_worker
import threading
from rich.progress import track

@tool
def request_to_search_swarm(tasks: list[str])->str:
    """Функция для выдачи задач поисковым агентам, принимает на вход список задач (максимум 6) в 
    формате строк и возвращает список ответов в формате строки: Ответ на задачу1: ответ\n Ответ на зхадчу 2: Ответ"""
    agent_count = 0
    threads: list[Any] = []
    answers: list[Any] = []
    for task in tasks: 
        agent_count += 1
        thread: Thread = threading.Thread(target=search_worker, args=(task, answers))
        threads.append(thread)
        thread.start()
    for thr in threads:
        thr.join()
    return "\n".join(answers)


@tool
def request_to_simple_swarm(tasks: list[str])->str:
    """Функция для выдачи задач агентам работникам, принимает на вход список задач (максимум 10) в 
    формате строк и возвращает список ответов в формате строки: Ответ на задачу1: ответ\n Ответ на зхадчу 2: Ответ"""
    agent_count = 0
    threads: list[Any] = []
    answers: list[Any] = []
    for task in tasks: 
        agent_count += 1
        thread: Thread = threading.Thread(target=simple_worker, args=(task, answers))
        threads.append(thread)
        thread.start()
    for thr in threads:
        thr.join()
    return "\n".join(answers)