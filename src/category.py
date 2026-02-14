from logging import exception

from src.product import Product


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products=None):
        self.name = name
        self.description = description
        self.__products = []
        if products:
            for product in products:
                if product.quantity > 0:
                    self.add_product(product)
                else:
                    raise ValueError


        Category.category_count += 1


    def __str__(self):
        return f'Название категории: {self.name}, количество продуктов: {self.products_count} шт.'

    def middle_price(self):
        """  функция вычисляет среднюю цену товаров в категории."""
        valid_price = []
        for product in self.__products:
            try:
                price = product.price
                price = float(price)
                if price < 0:
                    raise ValueError("Цена не может быть отрицательной")
                valid_price.append(price)
            except AttributeError:
                print(f'У товара {product} нет атрибута price')
            except ValueError:
                print(f'Не правильная цена у товара{product}')
            except Exception as e:
                print(f"Другая ошибка при обработке товара {product}")
        if not valid_price:
            return 0
        return sum(valid_price) / len(valid_price)


    def add_product(self, product: Product) -> None:
        """Добавляет товар в категорию с проверкой дубликатов"""
        if not issubclass(type(product), Product):
            raise TypeError("Можно добавлять только объекты "
                            "типа Product или его наследников")

        for existing_product in self.__products:
            if existing_product.name.lower() == product.name.lower():

                existing_product.quantity += product.quantity

                if product.price > existing_product.price:
                    existing_product.price = product.price

                existing_product.description = product.description
                print(f"Товар '{product.name}' уже существует. Количество увеличено до {existing_product.quantity}")
                return

        self.__products.append(product)
        Category.product_count += 1
        print(f"Товар '{product.name}' успешно добавлен")

    def __iter__(self):
        from src.categoryIterator import CategoryIterator
        return CategoryIterator(self)

    def get_product(self, index: int) -> Product | None:
        """Возвращает продукт по индексу, если индекс корректен"""
        if 0 <= index < len(self.__products):
            return self.__products[index]
        return None

    @property
    def products(self) -> str:
        """Property для отображения списка товаров"""
        result = []
        for product in self.__products:
            result.append(f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.')
        return "\n".join(result)

    def get_products_list(self) -> list[Product]:
        """Возвращает исходный список объектов товаров"""
        return self.__products

    @property
    def products_count(self) -> int:
        """Возвращает количество товаров в категории"""
        return len(self.__products)
