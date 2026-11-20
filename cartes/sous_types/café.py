from ..tasse import Tasse


class Cafe(Tasse):
    def __init__(self, prix: int, numero: list):
        super().__init__("Cafe", 2, [3])
