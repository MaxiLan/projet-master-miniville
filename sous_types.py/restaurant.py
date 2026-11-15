class Restaurant(Tasse):
    def __init__(self,prix):
        super().__init__("Restaurant",3)
    
    @property
    def nom(self):
        return self._nom
    
    @property
    def typ(self):
        return self._typ
        
    @property
    def prix(self):
        return self._prix