# Homework 10.2

## Описание:

Homework 10.2 - это проекта виджета банковских операций клиента. В нем содержатся следующие функции:
1. Функция маскировки номера счета или карты в masks.py
2. Функция маскировки счета или карты и получения точной даты в widget.py
3. Функция представления выполненных или невыполненных операций с сортировкой по дате в processing.py
4. Функция представляет информацию о транзакциях и генерирует номер карты в generators.py
5. Декоратор, регистрирующий детали выполнения функций, такие как время вызова, имя функции, передаваемые аргументы, 
результат выполнения и информация об ошибках в decorators.py 
6. Функция чтения JSON-файлов в utils.py
7. Функция вывода суммы транзакции в RUB по id-номеру. 
В случае, если сумма транзакции представлена в USD или EUR, выполняется функция конвертации с обращением к внешнему API.
Обе функции представлены в модуле external_api.py
8. Функции, выполняющие чтение csv и excel файлов в file_reader.py 

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/knewtr/homework10.1
```
2. Установите зависимости:
```
poetry install
```

## Использование:
Для использования необходимо находиться в директории src
### Для маскировки номера счета или номера карты:
* В функции get_mask_card_number введите 16-значный код
* В функции get_mask_account введите 20-значный код
* Нажмите сочетание клавиш Shift+F10
* Получите замаскированный номер карты или счета в диалоговом окне
```
# ввод: 7365410843013587
# вывод: 7365 41** **** 3587
```
### Для маскировки счета или карты:
* В функции mask_account_card введите данные карты или счета
* Нажмите сочетание клавиш Shift+F10
* Получите замаскированные данные карты или счета в диалоговом окне
```
# ввод: Visa Classic 6831982476737658 или Счет 64686473678894779589
# вывод: Visa Classic 6831 98** **** 7658 или Счет **9589
```
* В функции get_date введите данные
* Нажмите сочетание клавиш Shift+F10
* Получите корректную дату в диалоговом окне

```
# ввод: 2024-03-11T02:26:18.671407
# вывод: 11.03.2024
```
### Для получения выполненных или невыполненных операций с сортировкой по времени
* Вызовите функцию filter_by_state
* Нажмите сочетание клавиш Shift+F10
* Получите данные в диалоговом окне
```
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```
* Вызовите функцию sort_by_date
* Нажмите сочетание клавиш Shift+F10
* Получите отсортированные по дате данные в диалоговом окне

### Для получения списка транзакций по заданной валюте
* Вызовите функцию filter_by_currency
* Введите код валюты
* Нажмите сочетание клавиш Shift+F10
* Получите данные в диалоговом окне
```
# вывод:
{ "id": 939719570,
  "state": "EXECUTED",
  "date": "2018-06-30T02:08:58.425572",
  "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
  "description": "Перевод организации",
  "from": "Счет 75106830613657916952",
  "to": "Счет 11776614605963066702",
 }
```

### Для получения описания транзакций
* Вызовите функцию transaction_descriptions
* Нажмите сочетание клавиш Shift+F10
* Получите данные в диалоговом окне

```
# вывод:
Перевод организации
Перевод со счета на счет
Перевод со счета на счет
Перевод с карты на карту
Перевод организации
```

### Для получения номера карты
* Вызовите функцию card_number_generator
* Нажмите сочетание клавиш Shift+F10
* Получите данные в диалоговом окне

```
# вывод:
0000 0000 0000 0001
0000 0000 0000 0002
0000 0000 0000 0003
```

### Для чтения JSON-файла
* Вызовите функцию read_json_file
* Укажите путь к JSON-файлу
* Нажмите сочетание клавиш Shift+F10
* Получите данные в диалоговом окне

### Для вывода суммы транзакции в RUB
* Вызовите функцию get_transaction_rub
* Нажмите сочетание клавиш Shift+F10
* Получите данные в диалоговом окне

### Для чтения csv файлов
* Вызовите функцию get_transaction_csv
* Укажите путь к CSV-файлу
* Нажмите сочетание клавиш Shift+F10
* Получите данные в диалоговом окне

### Для чтения excel файлов
* Вызовите функцию get_transaction_csv
* Укажите путь к CSV-файлу
* Нажмите сочетание клавиш Shift+F10
* Получите данные в диалоговом окне

## Тестирование
Для запуска тестов необходимо находиться в директории tests
* Установите фреймворк pytest
* Выберите файл в наименовании которого есть 'test_'
* Введите в терминале pytest + test_наименование_функции.py
```
# пример ввода
pytest test_masks.py
```

## Логирование
При запуске функции masks.py или read_json_file в отдельном файле с расширением .log в папке logs
выводится информация о запуске и завершении работы функции с указанием 
времени, наименовании файла, уровне и самом сообщении.
```
2024-09-22 21:35:50,736 utils.py INFO: Opening the file
2024-09-22 21:35:50,737 utils.py INFO: Loading JSON-file
```
Для работы необходимо импортировать библиотеку logging
```
import logging
```
Установить необходимые параметры:
```
# пример
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(filename)s %(levelname)s: %(message)s",
    filename="../logs/utils.log",
    filemode="w",
)
```


## Документация:

Для получения дополнительной информации обратитесь к [документации](README.md).