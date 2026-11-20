from carte import Carte


class Vache(Carte):
    def __init__(self, nom: str, prix: int, numeros: list):
        super().__init__(nom, "Vache", prix, numeros)
