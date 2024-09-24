import pandas as pd


def get_transaction_csv(path: str) -> list[dict]:
    """Функция считывает данные о транзакциях из файла CSV"""
    try:
        csv_data_file = pd.read_csv(path, delimiter=";")
        csv_data_dict = csv_data_file.to_dict(orient="records")
        return csv_data_dict
    except FileNotFoundError:
        return []


def get_transaction_xlsx(path: str) -> list[dict]:
    """Функция считывает данные о транзакциях из файла XLSX"""
    try:
        xlsx_data_file = pd.read_excel(path)
        xlsx_data_dict = xlsx_data_file.to_dict(orient="records")
        return xlsx_data_dict
    except FileNotFoundError:
        return []
