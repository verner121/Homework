import unittest
from unittest.mock import mock_open, patch

from src.external_api import convert_to_rub
from src.utils import load_transactions


class TestUtils(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="[]")
    def test_load_transactions_empty_file(self, mock_file):
        """Проверяем, что результат пустой список"""
        result = load_transactions("data/operations.json")
        self.assertEqual(result, [])

    @patch("builtins.open", new_callable=mock_open, read_data="not a json")
    def test_load_transactions_invalid_json(self, mock_file):
        """Проверяем, что результат пустой список при некорректном JSON"""
        result = load_transactions("data/operations.json")
        self.assertEqual(result, [])

    @patch("os.path.isfile", return_value=False)
    def test_load_transactions_file_not_exist(self, mock_isfile):
        """Проверяем, что результат пустой список если файл не существует"""
        result = load_transactions("data/operations.json")
        self.assertEqual(result, [])

    @patch("builtins.open", new_callable=mock_open, read_data='{"amount": 100, "currency": "USD"}')
    def test_load_transactions_not_a_list(self, mock_file):
        """Проверяем, что результат пустой список если данные не список"""
        result = load_transactions("data/operations.json")
        self.assertEqual(result, [])

    @patch("requests.get")
    def test_convert_to_rub(self, mock_get):
        """Симулируем ответ API и проводим тестовую транзакцию"""
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"result": 7500}

        transaction = {"amount": 100, "currency": "USD"}
        result = convert_to_rub(transaction)
        self.assertEqual(result, 7500.0)  # Проверяем, что результат конвертации равен 7500


if __name__ == "__main__":
    unittest.main()  # Запуск тестов
