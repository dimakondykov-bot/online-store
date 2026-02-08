import os
import tempfile
import json
from src.utils import load_json_from_file


def test_valid_json():
    """Проверка на валидный json"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        test_data = ["apple", "banana", "orange"]
        json.dump(test_data, f)
        file_path = f.name
    try:
        result = load_json_from_file(file_path)
        assert result == test_data
    finally:
        os.remove(file_path)


def test_file_not_found():
    """Проверка на существование файла"""
    result = load_json_from_file("not_found.json")
    assert result == []


def test_invalid_json():
    """Проверка на не правильный json"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        f.write("test")
        file_path = f.name

    try:
        result = load_json_from_file(file_path)
        assert result == []
    finally:
        os.remove(file_path)


def test_empty_json():
    """Проверка на пустой файл"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        f.write("test")
        file_path = f.name

    try:
        result = load_json_from_file(file_path)
        assert result == []
    finally:
        os.remove(file_path)
