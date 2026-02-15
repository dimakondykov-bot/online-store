import pytest
from src.product import Product
from src.category import Category


def test_middle_price():
    """Средняя цена при корректных данных"""
    test_cat = Category("Продукты", "Описание")

    product_1 = Product("Хлеб", "Свежий", 45, 3)
    product_2 = Product("Колбаса", "Варёная", 450, 1)

    test_cat.add_product(product_1)
    test_cat.add_product(product_2)

    assert test_cat.middle_price() == (45 + 450) / 2


def test_middle_price_empty():
    """Если товаров нет — средняя цена 0"""
    test_cat = Category("Продукты", "Описание")
    assert test_cat.middle_price() == 0


def test_middle_price_incorrect_type():
    """Товар с некорректной ценой игнорируется"""
    test_cat = Category("Продукты", "Описание")

    product_1 = Product("Хлеб", "Свежий", 45, 3)
    product_2 = Product("Колбаса", "Варёная", "agsfbdsfger", 1)

    test_cat.add_product(product_1)
    test_cat.add_product(product_2)

    assert test_cat.middle_price() == 45


def test_negative_price():
    """Отрицательная цена игнорируется"""
    test_cat = Category("Продукты", "Описание")

    product_1 = Product("Хлеб", "Свежий", 45, 3)
    product_2 = Product("Колбаса", "Варёная", -450, 1)

    test_cat.add_product(product_1)
    test_cat.add_product(product_2)

    assert test_cat.middle_price() == 45


def test_none_price():
    """Цена None игнорируется"""
    test_cat = Category("Продукты", "Описание")

    product_1 = Product("Хлеб", "Свежий", 45, 3)
    product_2 = Product("Колбаса", "Варёная", None, 1)

    test_cat.add_product(product_1)
    test_cat.add_product(product_2)

    assert test_cat.middle_price() == 45
