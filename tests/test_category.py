from src.category import Category
from src.product import Product


def test_category_creation(sample_category: Category):

    assert sample_category.name == "Electronics"
    assert len(sample_category.get_products_list()) == 5
    assert Category.total_categories == 2
    assert Category.total_products == 5

def test_category_with_empty_products():

    category = Category("Books", "Various books")
    assert len(category.products) == 0
    assert Category.total_products == 0

def test_category_add_product(sample_category: Category, sample_product: Product):

    initial_count = len(sample_category.get_products_list())
    sample_category.get_products_list().append(sample_product)
    assert len(sample_category.get_products_list()) == initial_count + 1