from abc import ABC

from cartes.carte import Carte


class Antenne(Carte, ABC):
    def __init__(self, nom: str, prix: int, numeros: list):
        super().__init__(nom, "Antenne", prix, numeros)
