from abc import ABC, abstractmethod


class Carte(ABC):
    def __init__(self, nom: str, type: str, prix: int, numeros: list):
        self._nom = nom
        self._type = type
        self._prix = prix
        self._numeros = numeros
        self._activable = False

    @property
    def nom(self):
        return self._nom

    @property
    def type(self):
        return self._type

    @property
    def prix(self):
        return self._prix

    @property
    def numeros(self):
        return self._numeros

    @property
    def activable(self):
        return self._activable

    @abstractmethod
    def effet(self, joueur_t, joueur_p, liste_joueurs, banque, reserve):
        """Execute l'effet de la carte
        -joueur_t: joueur dont c'est le tour
        -joueur_p: joueur qui possède la carte
        -liste_joueurs: liste des joueurs de la partie
        -banque: Banque de la partie
        -reserve: Réserve de la partie
        """
        pass
