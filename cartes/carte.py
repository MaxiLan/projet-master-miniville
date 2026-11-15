from abc import ABC, abstractmethod
class Carte(ABC):
    def __init__(self,nom:str,typ:str,prix:int):
        self._nom=nom
        self._type=typ
        self._prix=prix

    @property
    def nom(self):
        return self._nom
    
    @property
    def typ(self):
        return self._typ

    @property
    def prix(self):
        return self._prix 
        
    @abstractmethod
    def effet(self):
        pass