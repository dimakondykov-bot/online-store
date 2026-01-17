from src.product import Product
from tests.convtest import simple_product


def test_product(simple_product):

    assert simple_product.name == "test_product"
    assert simple_product.description == "test_product"
    assert simple_product.price == 100
    assert simple_product.quantity == 1


def test_product_default_quantity():

    product = Product("Test", "Desc", 500.0)
    assert product.quantity == 0