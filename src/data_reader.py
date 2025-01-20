import pandas as pd
import os


def read_transactions_from_csv(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'файл {file_path} не найден')

    try:
        df = pd.read_csv(file_path)
        transactions = df.to_dict(orient="records")
        return transactions

    except Exception as e:
        f"Ошибка при чтении файла {file_path}: {e}"
        raise


def read_transactions_from_excel(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл {file_path} не найден.")
    try:
        df = pd.read_excel(file_path)
        transactions = df.to_dict(orient="records")
        return transactions
    except Exception as e:
        f"Ошибка при чтении файла {file_path}: {e}"
        raise
