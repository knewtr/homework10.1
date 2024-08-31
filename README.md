# Homework 10.1

## Описание:

Homework 10.1 - это часть проекта виджета банковских операций клиента, которая содержит две функции:
1. filter_by_state - принимает список словарей и выводит новый список словарей, содержащий
    только те словари, у которых ключ 'state' соответствует заданному значению.
2. sort_by_date - принимает список словарей и возвращает новый список,
    отсортированный по дате.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/knewtr/homework10.1
```
2. Установите зависимости:
```
pip install -r requirements.txt
```

## Как работают функции:

1. Функция filter_by_state принимает данные:
```
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```
И возвращает только со статусом 'EXECUTED':
```
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```
2. Функция sort_by_date принимает данные:
```
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```
И сортирует их по дате по убыванию
```
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```

## Документация:

Для получения дополнительной информации обратитесь к [документации](docs/README.md).
