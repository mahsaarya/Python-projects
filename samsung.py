from mobile import Mobile


class Samsung(Mobile):
    def __init__(self, name, price, voltage, screen_size, foldable):
        super().__init__(name, price, voltage, screen_size)
        self.foldable = foldable