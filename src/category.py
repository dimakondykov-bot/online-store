from src.product import Product


class Category:
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.total_categories += 1
        Category.total_products += len(self.__products)

    def __str__(self):
        return f'Название категории: {self.name}, количество продуктов: {self.products_count} шт.'

    def add_product(self, product):
        """Добавляет товар в категорию с проверкой дубликатов"""
        if not issubclass(type(product), Product):
            raise TypeError("Можно добавлять только объекты типа Product или его наследников")

        for existing_product in self.__products:
            if existing_product.name.lower() == product.name.lower():

                existing_product.quantity += product.quantity

                if product.price > existing_product.price:
                    existing_product.price = product.price

                existing_product.description = product.description
                print(f"Товар '{product.name}' уже существует. Количество увеличено до {existing_product.quantity}")
                return

        self.__products.append(product)
        Category.total_products += 1
        print(f"Товар '{product.name}' успешно добавлен")

    def get_product(self, index: int):
        """Возвращает продукт по индексу, если индекс корректен"""
        if 0 <= index < len(self.__products):
            return self.__products[index]
        return None

    @property
    def products(self):
        """Property для отображения списка товаров"""
        result = []
        for product in self.__products:
            result.append(f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.')
        return "\n".join(result)

    def get_products_list(self):
        """Возвращает исходный список объектов товаров"""
        return self.__products

    @property
    def products_count(self):
        """Возвращает количество товаров в категории"""
        return len(self.__products)

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.__products)}"
