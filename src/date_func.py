import datetime


def get_date(date_str: str) -> datetime:
    """Функция выводит дату в нужном формате"""
    if len(date_str) == 26:
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
        formated_date = date_obj.strptime("%d.%m.%Y")
        return formated_date
    else:
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S:%SZ")
        formated_date = date_obj.strptime("%d.%m.%Y")
        return formated_date
