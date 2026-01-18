import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def simple_product():
    return Product(
        name="test_product",
        description="test_product",
        price=500,
        quantity=3,
    )

@pytest.fixture
def sample_product():
    return Product("Laptop", "Gaming laptop", 1500.0, 8)

@pytest.fixture
def sample_category():
    products = [
        Product("Phone 1", "Desc 1", 1000.0, 10),
        Product("Phone 2", "Desc 2", 2000.0, 5),
        Product("Phone 3", "Desc 3", 3000.0, 2),
        Product("Phone 4", "Desc 4", 4000.0, 1),
        Product("Phone 5", "Desc 5", 5000.0, 3)
    ]
    # Create another category first to make total_categories == 2
    Category("Books", "Various books")
    return Category("Electronics", "Electronic devices", products)


@pytest.fixture(autouse=True)
def reset_counters():
    Category.total_categories = 0
    Category.total_products = 0
    yield
