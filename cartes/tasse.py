from cartes.carte import Carte


class Tasse(Carte):
    def __init__(self, nom: str, prix: int, numeros: list):
        super().__init__(nom, "Tasse", prix, numeros)
