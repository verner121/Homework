import os
import re
from typing import Dict, List

import pandas as pd


def read_transactions_from_csv(file_path: str) -> List[Dict]:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл {file_path} не найден.")
    try:
        df = pd.read_csv(file_path)
        transactions = df.to_dict(orient="records")
        return transactions
    except Exception as e:
        f"Ошибка при чтении файла {file_path}: {e}"
        raise


def read_transactions_from_excel(file_path: str) -> List[Dict]:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл {file_path} не найден.")
    try:
        df = pd.read_excel(file_path)
        transactions = df.to_dict(orient="records")
        return transactions
    except Exception as e:
        f"Ошибка при чтении файла {file_path}: {e}"
        raise


def filter_transactions(transactions: List[Dict], search_string: str) -> List[Dict]:
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)  # Компилируем шаблон
    filtered_transactions = [
        transaction for transaction in transactions if pattern.search(transaction.get("description", ""))
    ]
    return filtered_transactions


def count_transactions_by_category(transactions: List[Dict], categories: List[str]) -> Dict[str, int]:
    category_count = {category: 0 for category in categories}
    for transaction in transactions:
        description = transaction.get("description", "").lower()
        for category in categories:
            if category.lower() in description:
                category_count[category] += 1
    return category_count
