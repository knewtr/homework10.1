import json
from typing import Any


def read_json_file(path: str) -> Any:
    """Функция принимает путь до JSON-файла и возвращает список словарей с транзакциями"""
    try:
        with open(path, "r", encoding="utf-8") as file:
            try:
                transaction_data = json.load(file)
                return transaction_data
            except json.JSONDecodeError:
                transaction_data = []
                return transaction_data
    except FileNotFoundError:
        return []
