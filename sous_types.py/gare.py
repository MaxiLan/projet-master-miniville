class Gare(Monument):
    def __init__(self,prix):
        super().__init__("Gare",4)
    
    @property
    def nom(self):
        return self._nom
    
    @property
    def typ(self):
        return self._typ
        
    @property
    def prix(self):
        return self._prix