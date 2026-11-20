from ..antenne import Antenne


class Special(Antenne):
    def __init__(self, nom: str, prix: int, numeros: list):
        super().__init__(nom, prix, numeros)
