class Mine(Roue):
    def __init__(self,prix):
        super().__init__("Mine",6)
    
    @property
    def nom(self):
        return self._nom
    
    @property
    def typ(self):
        return self._typ
        
    @property
    def prix(self):
        return self._prix