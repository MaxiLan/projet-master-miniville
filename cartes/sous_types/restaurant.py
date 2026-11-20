from ..tasse import Tasse


class Restaurant(Tasse):
    def __init__(self, prix: int, numero: list):
        super().__init__("Restaurant", 3, [9, 10])
