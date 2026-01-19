from src.category import Category


def test_category_creation(sample_category):

    assert sample_category.name == "Electronics"
    assert len(sample_category.product_list) == 5
    assert Category.total_categories == 2
    assert Category.total_products == 5

def test_category_with_empty_products():

    category = Category("Books", "Various books")
    assert len(category.products) == 0
    assert Category.total_products == 0

def test_category_add_product(sample_category, sample_product):

    initial_count = len(sample_category.product_list)
    sample_category.product_list.append(sample_product)
    assert len(sample_category.product_list) == initial_count + 1