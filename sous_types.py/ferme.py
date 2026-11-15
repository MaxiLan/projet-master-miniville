class Ferme(Vache):
    def __init__(self,prix):
        super().__init__("Ferme",1)
    
    @property
    def nom(self):
        return self._nom
    
    @property
    def typ(self):
        return self._typ
        
    @property
    def prix(self):
        return self._prix