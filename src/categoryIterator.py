from src.category import Category


class CategoryIterator:
    def __init__(self, category):
        self.category: Category = category
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.category.products_count:
            product = self.category.get_product(self.index)
            self.index += 1
            return product
        else:
            raise StopIteration
