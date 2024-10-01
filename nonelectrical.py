from product import Product


class NonElectrical(Product):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight