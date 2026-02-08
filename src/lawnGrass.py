from src.product import Product
from src.base_product import BaseProduct


class LawnGrass(Product, BaseProduct):
    def __init__(self,
                 name,
                 description,
                 price,
                 quantity,
                 country,
                 germination_period,
                 color,
                 ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

