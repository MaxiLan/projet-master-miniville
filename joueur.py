class Joueur:
    def __init__(self,nom):
        self._nom=nom
        self._liste_cartes=[]
    
    def agir(self):
        n=de.lancer()
