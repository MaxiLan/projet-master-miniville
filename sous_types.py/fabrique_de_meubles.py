class Fabrique_de_meubles(Usine):
    def __init__(self,prix:int,numero:list):
        super().__init__("Fabrique de meubles",3,[8])
    
    @property
    def nom(self):
        return self._nom
    
    @property
    def typ(self):
        return self._typ
        
    @property
    def prix(self):
        return self._prix