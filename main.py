import json

# Чтение JSON файла
with open('books (1).json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Функция для рекурсивной обработки всех строк в структуре данных
def remove_special_chars(obj):
    if isinstance(obj, dict):
        return {key: remove_special_chars(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [remove_special_chars(item) for item in obj]
    elif isinstance(obj, str):
        return obj.replace('\u00A0', '').replace('\u000A', ' ')  # Удаляем \u00A0 (неразрывный пробел) и \u000A (новая строка)
    return obj

# Убираем спецсимволы из данных
clean_data = remove_special_chars(data)

# Выводим очищенные данные
print(clean_data)
