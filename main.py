from typing import Any

from src.date_func import get_date
from src.file_reader import get_transaction_csv, get_transaction_xlsx
from src.processing import filter_by_state
from src.search_funcs import transaction_category
from src.utils import read_json_file
from src.widget import mask_account_card

print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
print(
    "Выберите необходимый пункт меню:"
    "\n1. Получить информацию о транзакциях из JSON-файла"
    "\n2. Получить информацию о транзакциях из CSV-файла"
    "\n3. Получить информацию о транзакциях из XLSX-файла"
)

choose_file_input = input()

while True:
    choose_file_input = input()
    if choose_file_input == "1":
        print("Для обработки выбран JSON-файл")
        break
    elif choose_file_input == "2":
        print("Для обработки выбран CSV-файл")

        break
    elif choose_file_input == "3":
        print("Для обработки выбран XLSX-файл")

    else:
        continue

choose_file_input = input()


def get_transactions(file_input: str) -> Any:
    if file_input == "1":
        transactions = read_json_file("../data/operations.json")
        return transactions
    elif file_input == "2":
        transactions = get_transaction_csv("../data/operations_excel.csv")
        return transactions
    elif file_input == "3":
        transactions = get_transaction_xlsx("../data/operations_excel.xlsx")
        return transactions


work_process_1 = get_transactions(choose_file_input)
print(
    "Введите статус, по которому необходимо выполнить фильтрацию. "
    "\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
)

search_input = input()

while True:
    if search_input.upper() == "EXECUTED":
        print("Операции отфильтрованы по статусу EXECUTED")
        break
    elif search_input.upper() == "CANCELED":
        print("Операции отфильтрованы по статусу CANCELED")
        break
    elif search_input.upper() == "PENDING":
        print("Операции отфильтрованы по статусу PENDING")
        break
    else:
        print(f"Статус операции {search_input} недоступен.")
        print(
            "Введите статус, по которому необходимо выполнить фильтрацию."
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
        )
        search_input = input()

work_process_2 = filter_by_state(work_process_1, search_input)

print("Отсортировать операции по дате? Да/Нет")
sorting_date_input = input()
if sorting_date_input.lower() == "да":
    print("Отсортировать по возрастанию или по убыванию?")
    sort_up_down = input()
    if sort_up_down.lower() != "по возрастанию" and sort_up_down.lower() != "по убыванию":
        print('Введите: "по возрастанию" или "по убыванию"')
        sort_up_down = input()
elif sorting_date_input.lower() == "нет":
    sort_up_down = ""


def sort_transactions_by_date(transactions: list[dict], sorting_date_input: str) -> Any:
    new_transactions = []
    if sorting_date_input.lower() == "да":
        for transaction in transactions:
            if transaction["operationAmount"]["currency"]["code"] == "RUB":
                new_transactions.append(transaction)
                return new_transactions
    else:
        return transactions


work_process_3 = sort_transactions_by_date(work_process_2, sorting_date_input, sort_up_down)

print("Выводить только рублевые транзакции? Да/Нет")
sorting_rub_input = input()


def transaction_list_rub(transactions: list[dict], user_input: str) -> Any:
    new_transactions = []
    if user_input.lower() == "да":
        for transaction in transactions:
            if transaction["operationAmount"]["currency"]["code"] == "RUB":
                new_transactions.append(transaction)
                return new_transactions
            else:
                return transactions


work_process_4 = transaction_list_rub(work_process_3, sorting_rub_input)

print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
filter_input = input()
if filter_input.lower() == "да":
    word_input = input()
    print(
        """Доступные для фильтровки описания: Открытие вклада, Перевод организации, Перевод с карты на карту,
            Перевод со счета на счет"""
    )
elif filter_input.lower() == "нет":
    total_transaction_list = work_process_4


def transaction_list_by_word(transactions: list[dict], user_input: str, word_search: str) -> Any:
    if user_input.lower() == "да":
        total_transaction_list = transaction_category(transactions, word_search)
        return total_transaction_list
    elif user_input.lower() == "нет":
        return transactions


work_process_5 = transaction_list_by_word(work_process_4, filter_input, word_input)

print('\nРаспечатываю итоговый список транзакций...')
print(f'Всего банковских операций в выборке: {len(work_process_5)}')


def format_transactions(total_transaction_list: list[dict]) -> str:
    if len(total_transaction_list) == 0:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        for transaction in total_transaction_list:
            date = get_date(transaction["date"])
            description = transaction["description"]
            if description == "Открытие вклада":
                account_number = mask_account_card(transaction["to"])
                return account_number
            elif description != "Открытие вклада":
                card_account_number_1 = mask_account_card(transaction["from"])
                card_account_number_2 = mask_account_card(transaction["to"])
                output_card = f"{card_account_number_1} -> {card_account_number_2}"
            transaction_sum = transaction["operationAmount"]["amount"]
            transaction_currency = transaction["operationAmount"]["currency"]["name"]
            return f"{date} {description} \n{output_card} " f"\nСумма: {transaction_sum} {transaction_currency}"
