from src.product import Product
import pytest

def test_product(simple_product: Product):
    assert simple_product.name == "test_product"
    assert simple_product.description == "test_product"
    assert simple_product.price == 500
    assert simple_product.quantity == 3


def test_product_default_quantity(simple_product: Product):
    product = Product("Test", "Desc", 500.0)
    assert product.quantity == 0

def test_product_total_cost(simple_product: Product):

    total = simple_product.total_cost()
    assert total == 1500.0
    assert simple_product.quantity * simple_product.price

def test_add_product(simple_product: Product):
    product = Product("Test", "Desc", 500.0)
    other_obj = "это не продукт"

    with pytest.raises(TypeError):
        result = product + other_obj

def test_product_str(simple_product: Product):
    product = Product("Виноград", "с косточкой", 350,5)

    str_result = str(product)
    expected = "Виноград, 350 руб., Остаток: 5 шт"
    assert str_result == expected, f"Неверный формат: {str_result}"