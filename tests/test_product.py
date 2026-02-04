from src.product import Product


def test_product(simple_product: Product):
    assert simple_product.name == "test_product"
    assert simple_product.description == "test_product"
    assert simple_product.price == 500
    assert simple_product.quantity == 3


def test_product_default_quantity():
    product = Product("Test", "Desc", 500.0)
    assert product.quantity == 0
