from src.category import Category


class Product:
    name: str
    description: str
    price: float

    def __init__(self, name, description, price=0.0, quantity=0):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
