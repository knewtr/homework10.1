import re
from collections import Counter
from typing import Dict, List, Any

from src.utils import read_json_file


def search_transactions(trans_list: list, search_str: str) -> List[Dict] | Any:
    """Функция поиска транзакций по заданному описанию"""
    try:
        pattern = re.compile(search_str, re.IGNORECASE)
        filtered_transactions = [
            transaction for transaction in trans_list if pattern.findall(transaction["description"])
        ]
        return filtered_transactions
    except Exception as e:
        print("Ничего не найдено", e)
        return []


def transaction_category(trans_list: list, categories: list[str]) -> dict:
    """Функция вывода количества транзакций по различным категориям"""
    try:
        transaction_categories = [
            transaction["description"] for transaction in trans_list if transaction.get("description") in categories
        ]
        counted_categories = Counter(transaction_categories)
        return dict(counted_categories)
    except Exception as e:
        print("Произошла ошибка", e)
        return {}


# if __name__ == '__main__':
#     dict_1 = read_json_file('../data/operations.json')
#     list_cat = ["Открытие вклада", "Перевод с карты на карту", "Перевод со счета на счет"]
#     result = transaction_category(dict_1, list_cat)
#     print(result)
