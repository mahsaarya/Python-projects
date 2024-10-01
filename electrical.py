from product import Product


class Electrical(Product):
    def __init__(self, name, price, voltage):
        super().__init__(name, price)
        self.voltage = voltage

        @property
        def voltage(self):
            return

        @voltage.setter
        def voltage(self, value):
            pass