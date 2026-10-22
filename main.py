import re
import sys
import requests

# Шаблоны для различных форматов дат
DATE_PATTERNS = [
    r'\b\d{2}\.\d{2}\.\d{4}\b',  # ДД.ММ.ГГГГ
    r'\b\d{4}-\d{2}-\d{2}\b',  # ГГГГ-ММ-ДД
    r'\b\d{2}/\d{2}/\d{4}\b'   # ДД/ММ/ГГГГ
]

# Объединенный паттерн для поиска всех форматов
COMBINED_PATTERN = '|'.join(DATE_PATTERNS)

def validate_date(date_str):
    """Проверка строки на соответствие одному из форматов даты."""
    for pattern in DATE_PATTERNS:
        if re.fullmatch(pattern, date_str):
            return True
    return False

def search_dates(text):
    """Поиск всех дат в произвольном тексте."""
    return re.findall(COMBINED_PATTERN, text)

def search_in_file(filepath):
    """Поиск дат в локальном файле."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        return search_dates(content)
    except FileNotFoundError:
        return f"Ошибка: файл '{filepath}' не найден."

def search_in_url(url):
    """Поиск дат на веб-странице по URL."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return search_dates(response.text)
    except requests.RequestException as e:
        return f"Ошибка при запросе URL: {e}"

if __name__ == '__main__':
    print("=== Поиск и проверка дат с помощью регулярных выражений ===")
    print("1. Проверить строку (пользовательский ввод)")
    print("2. Найти даты в файле")
    print("3. Найти даты на веб-странице (URL)")
    
    choice = input("Выберите режим работы (1-3): ").strip()
    
    if choice == '1':
        user_input = input("Введите строку для проверки: ")
        if validate_date(user_input):
            print("Результат: Строка является корректной датой в одном из поддерживаемых форматов.")
        else:
            print("Результат: Строка НЕ соответствует ни одному формату даты.")
            
        found = search_dates(user_input)
        if found:
            print(f"Найденные даты в тексте: {found}")
            
    elif choice == '2':
        filepath = input("Введите путь к текстовому файлу: ").strip()
        result = search_in_file(filepath)
        print("Найденные даты:", result)
        
    elif choice == '3':
        url = input("Введите URL веб-страницы: ").strip()
        result = search_in_url(url)
        print("Найденные даты:", result)
        
    else:
        print("Неверный выбор режима.")