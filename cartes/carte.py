from abc import ABC, abstractmethod
class Carte(ABC):
    def __init__(self,nom:str,typ:str,prix:int):
        self._nom=nom
        self._type=typ
        self._prix=prix

    @abstractmethod
    def effet(self):
        pass