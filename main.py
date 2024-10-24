import json

with open('books (1).json', 'r', encoding='utf-8') as file:
    data = json.load(file)

def remove_special_chars(obj):
    if isinstance(obj, dict):
        return {key: remove_special_chars(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [remove_special_chars(item) for item in obj]
    elif isinstance(obj, str):
        return obj.replace('\u00A0', '').replace('\u000A', ' ')
    return obj


clean_data = remove_special_chars(data)


print(clean_data)
