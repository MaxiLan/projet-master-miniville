class Champs_de_ble(Ble):
    def __init__(self,prix):
        super().__init__("Champs de blé",1)
    
    @property
    def nom(self):
        return self._nom
    
    @property
    def typ(self):
        return self._typ
        
    @property
    def prix(self):
        return self._prix