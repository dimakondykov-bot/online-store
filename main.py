from src.categoryIterator import CategoryIterator
from src.category import Category
from src.product import Product


def main():
    product1 = Product('Product 1', 'Test product', 100.0, 1)
    product2 = Product('Product 2', 'Test product', 100.0, 1)
    product3 = Product('Product 3', 'Test product', 100.0, 1)

    category = Category('Products', 'Test category')
    category.add_product(product1)
    category.add_product(product2)
    category.add_product(product3)

    for item in CategoryIterator(category):
        print(item)


if __name__ == '__main__':
    main()
