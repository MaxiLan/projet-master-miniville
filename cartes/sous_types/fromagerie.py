from ..usine import Usine


class Fromagerie(Usine):
    def __init__(self, prix: int, numero: list):
        super().__init__("Fromagerie", 5, [7])
