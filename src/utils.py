import json


def load_json_from_file(path_to_file) -> list:
    try:
        with open(path_to_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"файл {path_to_file} не найден")
        return []
    except json.JSONDecodeError as e:
        print(f"ошибка JSON файла {path_to_file} {e}")
        return []
    except Exception as e:
        print(f"ошибка при чтении {path_to_file}: {e}")
        return []