from ..usine import Usine


class Fabrique_de_meubles(Usine):
    def __init__(self, prix: int, numero: list):
        super().__init__("Fabrique de meubles", 3, [8])
