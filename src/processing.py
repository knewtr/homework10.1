def filter_by_state(state_list: list[dict[str, str]]) -> list[dict[str, str]]:
    """Функия принимает список словарей и выводит новый список словарей, содержащий
    только те словари, у которых ключ 'state' соответствует заданному значению"""
    new_state_list: list = []
    for x in state_list:
        if x["state"] == "EXECUTED":
            new_state_list.append(x)
    return new_state_list


def sort_by_date(date_list: list[dict[str, str]]) -> list[dict[str, str]]:
    """Функция принимает список словарей и возвращает новый список,
    отсортированный по дате"""
    sorted_date_list = sorted(date_list, key=lambda x: x["date"], reverse=True)
    return sorted_date_list
