from carte import Carte


class Tomate(Carte):
    def __init__(self, nom: str, prix: int, numeros: list):
        super().__init__(nom, "Tomate", prix, numeros)
