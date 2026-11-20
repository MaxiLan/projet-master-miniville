from ..vache import Vache


class Ferme(Vache):
    def __init__(self, prix: int, numero: list):
        super().__init__("Ferme", 1, [2])
