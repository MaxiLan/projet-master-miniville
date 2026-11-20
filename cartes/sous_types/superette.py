from ..brioche import Brioche


class Superette(Brioche):
    def __init__(self, prix: int, numero: list):
        super().__init__("Superette", 4, [4])
