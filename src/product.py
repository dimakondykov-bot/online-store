class Product:
    def __init__(self, name, description, price=0.0, quantity=0):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}, {self.price} руб., Остаток: {self.quantity} шт'

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError
        return (self.__price * self.quantity) + (other.__price * other.quantity)

    @classmethod
    def new_product(cls, product_dict: dict, existing_products=None):
        """
        Создает новый товар или объединяет с существующим

        Args:
            product_dict: словарь с данными нового товара
            existing_products: список существующих товаров для проверки дубликатов
        """
        name = product_dict.get('name')
        if not name:
            raise ValueError('Поле "name" не может быть пустым или отсутствовать')

        description = product_dict.get('description')
        if description is None:
            raise ValueError('Поле "description" не может отсутствовать')

        price = product_dict.get('price')
        if price is None:
            raise ValueError('Поле "price" не может быть пустым или отсутствовать')

        quantity = product_dict.get('quantity')
        if quantity is None:
            raise ValueError('Поле "quantity" не может быть пустым или отсутствовать')

        if existing_products:
            for existing_product in existing_products:
                if existing_product.name.lower() == name.lower():
                    existing_product.quantity += quantity
                    if price > existing_product.price:
                        existing_product.price = price
                    existing_product.description = description

                    print(f"Товар '{name}' уже существует. Количество увеличено до {existing_product.quantity}")
                    return existing_product

        return cls(name, description, price, quantity)

    @property
    def price(self):
        """Геттер для получения цены"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер для установки цены с проверкой"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            answer = input(f"Цена снижается с {self.__price} до {new_price}. Подтвердить? (y/n): ")
            if answer.lower() != 'y':
                print("Изменение цены отменено")
                return

        self.__price = new_price

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."
