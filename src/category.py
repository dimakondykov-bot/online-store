

class Category():
    # атрибуты класса общие для всех объектов
    total_category_count = 0
    total_product_count = 0

    name: str
    description: str
    products: list

    def __init__(self,name,description,products=None):
        self.name = name
        self.description = description
        self.products = products if products else []

        Category.total_category_count += 1
        Category.total_product_count += len(self.products)

