from abc import ABC

from cartes.antenne import Antenne


class Monument(Antenne, ABC):
    def __init__(self, nom: str, prix: int):
        super().__init__(nom, prix, [])
        self.est_construit = False
