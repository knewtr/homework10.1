from src.date_func import get_date
from src.file_reader import get_transaction_csv, get_transaction_xlsx
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.utils import read_json_file
from src.widget import mask_account_card


def main():
    '''Основная функция проекта'''
    while True:
        print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
        print(
            "Выберите необходимый пункт меню:"
            "\n1. Получить информацию о транзакциях из JSON-файла"
            "\n2. Получить информацию о транзакциях из CSV-файла"
            "\n3. Получить информацию о транзакциях из XLSX-файла"
        )

        choose_file_input = input()
        if choose_file_input == "1":
            print("Для обработки выбран JSON-файл")
            transactions = read_json_file("../data/operations.json")
            break
        elif choose_file_input == "2":
            print("Для обработки выбран CSV-файл")
            transactions = get_transaction_csv("../data/operations_excel.csv")
            break
        elif choose_file_input == "3":
            print("Для обработки выбран XLSX-файл")
            transactions = get_transaction_xlsx("../data/operations_excel.xlsx")
        else:
            print("Ошибка. Введите необходимый пункт меню")


    while True:
        print(
            "Введите статус, по которому необходимо выполнить фильтрацию. "
            "\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
        )

        search_input = input()

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

        filtered_transactions = filter_by_state(transactions, search_input)

        print("Отсортировать операции по дате? Да/Нет")
        sorting_date_input = input()
        if sorting_date_input.lower() == "да":
            if input("Отсортировать по возрастанию или по убыванию?").lower() == "по возрастанию":
                sort_up_down = False
            else:
                sort_up_down = True
            filtered_transactions = sort_by_date(filtered_transactions, sort_up_down)

        print("Выводить только рублевые транзакции? Да/Нет")
        sorting_rub_input = input()
        if sorting_rub_input.lower() == "да":
            rub_transactions = filter_by_currency(filtered_transactions, "RUB")
            filtered_transactions = list(rub_transactions)

        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        print(
            """Доступные для фильтровки описания: Открытие вклада, Перевод организации, Перевод с карты на карту,
            Перевод со счета на счет"""
        )
        filter_input = input()
        if filter_input.lower() == "да":
            word = input("Введите слово ")
            filtered_transactions = filter_by_state(filtered_transactions, word)

        print("\nРаспечатываю итоговый список транзакций...")
        if len(filtered_transactions) == 0:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        else:
            print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
            for transaction in filtered_transactions:
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
