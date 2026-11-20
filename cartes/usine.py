from carte import Carte


class Usine(Carte):
    def __init__(self, nom: str, prix: int, numeros: list):
        super().__init__(nom, "Usine", prix, numeros)
