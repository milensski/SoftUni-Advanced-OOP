from project.product import Product


class Food(Product):

    def __init__(self, name):
        self.quantity = 15
        super().__init__(name, self.quantity)

