class Joueur:
    def __init__(self,nom:str,argent:int):
        self._nom=nom
        self._argent=3
        self._liste_cartes=[]
        
    def agir(self):
        n=de.lancer()

    def payer(self,somme:int):
        if self._argent<=somme:
            self._argent=0
        self._argent-=somme

    def recevoir(self,somme:int):
        self._argent+=somme
