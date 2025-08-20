from ddgs import DDGS

def duckduckgo_search(query: str) -> str:
    """
    Инструмент для поиска актуальной информации в интернете через DuckDuckGo.
    Принимает на вход поисковый зпрос (строку) и возвращает нумерованный список результатов.
    Каждый результат содержит заголовок, краткое описание (сниппет) и URL для дальнейшего анализа.
    """
    try:
        with DDGS() as ddgs:
            results = ddgs.text(query, region='ru-ru', max_results=5)
            
            if not results:
                return "По вашему запросу ничего не найдено."

            formatted_results = []
            for i, res in enumerate(results, 1):
                formatted_results.append(
                    f"Результат {i}:\n"
                    f"  Title: {res['title']}\n"
                    f"  Snippet: {res['body']}\n"
                    f"  URL: {res['href']}\n"
                )
            
            instruction = (
                "\n--- Инструкция для Агента ---\n"
                "Проанализируй заголовки и сниппеты. Если они кажутся релевантными, "
                "используй инструмент `scrape_webpage` с наиболее подходящим URL, чтобы получить полную информацию."
            )
            print(formatted_results)

            return "\n".join(formatted_results) + instruction
    except Exception as e:
        return f"Ошибка при выполнении поиска в DuckDuckGo: {e}"
    

print(duckduckgo_search("Самые популярные языки рпограммирования"))