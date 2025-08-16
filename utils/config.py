import json


def load(config_data_name: str)->str:
    with open("config.json", "r", encoding="utf-8") as f:
        config_data = json.load(f)
    config_data = config_data[config_data_name]
    return config_data

try:
    gemini_api_key = load("gemini_api_key")
    tavily_api_key = load("tavily_api_key")
except:
    gemini_api_key = "none"
    tavily_api_key = "none"