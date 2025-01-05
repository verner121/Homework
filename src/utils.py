import json
import os

path_to_file = os.path.join(os.path.dirname(__file__), "data", "..", "operations.json")


def list_dict_transaction(path_to_file):
    try:
        with open(path_to_file, "r", encoding='utf-8') as f:
            try:
                operation_file = json.load(f)
            except json.JSONDecodeError as e:
                print(f"Ошибка при декодировании JSON из файла {path_to_file}: {e}")
                return []
        if type(operation_file) == list:
            return operation_file
        else:
            return []
    except FileNotFoundError as e:
        print('Файл не найден')
        return []
