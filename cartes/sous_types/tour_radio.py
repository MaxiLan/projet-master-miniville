class Tour_radio(Monument):
    def __init__(self,prix:int):
        super().__init__("Tour radio",22)
    
    @property
    def nom(self):
        return self._nom
    
    @property
    def typ(self):
        return self._typ
        
    @property
    def prix(self):
        return self._prix