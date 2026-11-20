from ..roue import Roue


class Foret(Roue):
    def __init__(self, prix: int, numero: list):
        super().__init__("Roue", 3, [5])
