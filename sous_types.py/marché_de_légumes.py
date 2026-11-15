class Marche_de_legumes(Tomate):
    def __init__(self,prix):
        super().__init__("Marché de légumes",2)
    
    @property
    def nom(self):
        return self._nom
    
    @property
    def typ(self):
        return self._typ
        
    @property
    def prix(self):
        return self._prix