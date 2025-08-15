from langchain_community.tools import TavilySearchResults
from langchain_core.tools import Tool, tool
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

tavily_tool = TavilySearchResults(max_results=5)
tavily_tool.description = "Инструмент для поиска актуальной информации в интернете."

@tool
def scrape_webpage(url: str) -> str:
    """
    Инструмент, который загружает веб-страницу по URL и возвращает ее текстовое содержимое.
    Используйте его, чтобы получить детальную информацию со страницы, найденной с помощью поиска.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Проверка на ошибки HTTP

        soup = BeautifulSoup(response.text, "html.parser")

        # Удаляем ненужные теги (скрипты, стили)
        for script_or_style in soup(["script", "style"]):
            script_or_style.decompose()

        # Получаем текст и очищаем его
        text = " ".join(t.strip() for t in soup.stripped_strings)
        return f"Содержимое страницы {url}:\n\n{text}"

    except requests.RequestException as e:
        return f"Ошибка при загрузке страницы {url}: {e}"


