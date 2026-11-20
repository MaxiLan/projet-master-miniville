from ..roue import Roue


class Mine(Roue):
    def __init__(self, prix: int, numero: list):
        super().__init__("Mine", 6, [9])
