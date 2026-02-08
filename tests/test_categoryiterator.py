import pytest

from src import categoryIterator
from src.category import Category
from src.categoryIterator import CategoryIterator
from src.product import Product


def test_product_creation():
    """Тестируем создание объекта Product"""
    # Создаем продукт
    product = Product('Хлеб', 'Свежий хлеб', 47.0, 78)

    assert product.name == 'Хлеб'
    assert product.description == 'Свежий хлеб'
    assert product.price == 47.0
    assert product.quantity == 78


def test_one_product_in_category():
    """Тестируем итератор с одним продуктом"""
    # Создаем продукт
    product = Product('Банан', 'Желтый банан', 38.0, 44)

    category = Category('Фрукты', 'Свежие фрукты')

    category.add_product(product)

    iterator = CategoryIterator(category)

    product_from_iterator = next(iterator)

    assert product_from_iterator.name == 'Банан'
    assert product_from_iterator.description == 'Желтый банан'
    assert product_from_iterator.price == 38.0


def test_empty_category():
    """Что происходит с пустой категорией?"""

    category = Category('Пустая', 'Нет продуктов')
    iterator = CategoryIterator(category)

    try:
        next(iterator)
        assert False
    except StopIteration:
        pass


