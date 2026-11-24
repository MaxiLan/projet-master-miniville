from abc import ABC

from cartes.carte import Carte


class Vache(Carte, ABC):
    def __init__(self, nom: str, prix: int, numeros: list):
        super().__init__(nom, "Vache", prix, numeros)
