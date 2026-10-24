import unittest
from main import validate_date, search_dates

class TestDateRegex(unittest.TestCase):
    
    def test_validate_valid_dates(self):
        """Тест на валидацию корректных дат"""
        self.assertTrue(validate_date("31.12.2023"))
        self.assertTrue(validate_date("2023-12-31"))
        self.assertTrue(validate_date("15/05/2021"))

    def test_validate_invalid_dates(self):
        """Тест на валидацию некорректных строк"""
        self.assertFalse(validate_date("31-12-2023"))  # Неверный разделитель для первого формата
        self.assertFalse(validate_date("23.12.23"))     # Год из двух цифр
        self.assertFalse(validate_date("abc.de.ghij"))  # Буквы вместо цифр
        self.assertFalse(validate_date("31.12.2023.1")) # Лишние символы

    def test_search_dates_in_text(self):
        """Тест поиска нескольких дат в тексте"""
        text = ("Встреча назначена на 12.04.2024 или на 2024-04-15. "
                "Также упоминается старая дата 01/01/2020, а вот формат 31-12-2023 не должен найтись.")
        expected = ["12.04.2024", "2024-04-15", "01/01/2020"]
        self.assertEqual(search_dates(text), expected)

if __name__ == '__main__':
    unittest.main()
