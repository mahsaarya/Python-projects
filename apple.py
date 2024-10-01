from mobile import Mobile


class Apple(Mobile):
    def __init__(self, name, price, voltage, screen_size, country):
        super().__init__(name, price, voltage, screen_size)
        self.country = country