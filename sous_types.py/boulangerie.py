#Sous-sous classe Boulangerie
#faire une liste avec les joeurs de la partie, en faire un attribut dans cette classe, et trouver dans cette liste le joueur qui joue, pour lui verser l'argent ?
class Boulangerie(Brioche):
    def __init__(self,prix):
        super().__init__("Boulangerie",1)
    
    @property
    def nom(self):
        return self._nom
    
    @property
    def typ(self):
        return self._typ
        
    @property
    def prix(self):
        return self._prix

    
