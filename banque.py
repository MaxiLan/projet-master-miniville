class Banque:
    def __init__(self):
        self.argent = 171

    def recevoir(self, somme: int):
        self.argent += somme

    def payer(self, entite, somme: int):
        """Le joueur paye la banque ou un joueur
        -entite: désigne la banque ou un autre joueur
        -somme: somme à payer
        """
        q = min(somme, self.argent)
        self.argent -= q
        entite.recevoir(q)
        return q  # on renvoie le vrai montant payé
