from ..tomate import Tomate


class Marche_de_legumes(Tomate):
    def __init__(self, prix: int, numero: list):
        super().__init__("Marché de légumes", 2, [11, 12])
