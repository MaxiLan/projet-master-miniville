from abc import ABC, abstractmethod


class Carte(ABC):
    def __init__(self, nom: str, type: str, prix: int, numeros: list):
        self._nom = nom
        self._type = type
        self._prix = prix
        self._numeros = numeros

    @property
    def nom(self):
        return self._nom

    @property
    def typ(self):
        return self._type

    @property
    def prix(self):
        return self._prix

    @property
    def numeros(self):
        return self._numeros

    @abstractmethod
    def effet(self, joueur, liste_joueurs, banque, reserve):
        """Execute l'effet de la carte
        -joueur: joueur qui possède la carte
        -liste_joueurs: liste des joueurs de la partie
        -banque: Banque de la partie
        -reserve: Réserve de la partie
        """
        pass
