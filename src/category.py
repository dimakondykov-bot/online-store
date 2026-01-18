

class Category():
    # атрибуты класса общие для всех объектов
    total_categories = 0
    total_products = 0

    name: str
    description: str
    products: list

    def __init__(self,name,description,products=None):
        self.name = name
        self.description = description
        self.products = products if products else []

        Category.total_categories += 1
        Category.total_products += len(self.products)

