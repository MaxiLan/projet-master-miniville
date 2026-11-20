class Verger(Ble):
    def __init__(self,prix:int,numero:list):
        super().__init__("Verger",3,[10])
    
    @property
    def nom(self):
        return self._nom
    
    @property
    def typ(self):
        return self._typ
        
    @property
    def prix(self):
        return self._prix