class Parc_d_attractions(Monument):
    def __init__(self,prix):
        super().__init__("Parc d'attractions",16)
    
    @property
    def nom(self):
        return self._nom
    
    @property
    def typ(self):
        return self._typ
        
    @property
    def prix(self):
        return self._prix