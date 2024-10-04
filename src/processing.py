from typing import Any


def filter_by_state(state_list: list[dict[str, Any]], default_state: str = "EXECUTED") -> list[str]|Any:
    """Функия принимает список словарей и выводит новый список словарей, содержащий
    только те словари, у которых ключ 'state' соответствует заданному значению"""
    new_state_list: list = []
    for dictionary in state_list:
        if dictionary["state"] == default_state:
            new_state_list.append(dictionary)
        else:
            return new_state_list
    return new_state_list


def sort_by_date(
    date_list: list[dict[str, Any]], reversed_list: bool = True
) -> list[dict[str, Any]]:
    """Функция принимает список словарей и возвращает новый список,
    отсортированный по дате"""
    sorted_date_list = sorted(date_list, key=lambda x: x["date"], reverse=reversed_list)
    return sorted_date_list
