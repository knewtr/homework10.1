import os
from typing import Any

import requests
from dotenv import load_dotenv
from requests import RequestException
from typing_extensions import Optional

# from src.utils import read_json_file

load_dotenv()
api_key = os.getenv("API_KEY")


def get_transaction_rub(transactions: list, transaction_id: int) -> Optional[float]:
    """Функция выводит сумму транзакции по id-номеру"""
    for transaction in transactions:
        if transaction.get("id") == transaction_id:
            if transaction["operationAmount"]["currency"]["code"] == "RUB":
                rub_amount = float(transaction["operationAmount"]["amount"])
                return rub_amount
        else:
            convert_transaction = {
                "amount": transaction["operationAmount"]["amount"],
                "currency": transaction["operationAmount"]["currency"]["code"],
            }
            return convert_to_rub(convert_transaction)


def convert_to_rub(convert_transaction: dict) -> Any:
    """Функция принимает значение в долларах или евро, обращается к внешнему API
    и возвращает сумму транзакции в рублях"""
    amount = convert_transaction["amount"]
    currency = convert_transaction["currency"]
    try:
        if currency == "USD":
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount={amount}"
        elif currency == "EUR":
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount={amount}"
        else:
            return None

        headers = {"apiKey": api_key}
        response = requests.get(url, headers=headers)
        json_result = response.json()

        return json_result["result"]
    except RequestException:
        return 0


# if __name__ == "__main__":
#    transactions = read_json_file('../data/operations.json')
#    print(get_transaction_rub(transactions, 41428829))
