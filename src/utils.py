import json
import logging
from typing import Any

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(filename)s %(levelname)s: %(message)s",
    filename="../logs/utils.log",
    filemode="w",
)

logger = logging.getLogger()


def read_json_file(path: str) -> Any:
    """Функция принимает путь до JSON-файла и возвращает список словарей с транзакциями"""
    try:
        logging.info("Opening the file")
        with open(path, "r", encoding="utf-8") as file:
            try:
                transaction_data = json.load(file)
                logging.info("Loading JSON-file")
                return transaction_data
            except json.JSONDecodeError:
                logging.info("JSONDecodeError")
                transaction_data = []
                return transaction_data
    except FileNotFoundError:
        logging.info("File Not Found")
        return []
