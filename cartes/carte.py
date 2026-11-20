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
    def effet(self):
        pass
