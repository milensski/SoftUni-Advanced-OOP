from project.product import Product


class ProductRepository:
    products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name):
        product = list(filter(lambda p: p.name == product_name, self.products))
        if product:
            return product[0]

    def remove(self, product_name):
        product = list(filter(lambda p: p.name == product_name, self.products))
        if product:
            self.products.remove(product[0])

    def __repr__(self):
        information = []
        for item in ProductRepository.products:
            information.append(f'{item.name}: {item.quantity}')
        return '\n'.join(information)