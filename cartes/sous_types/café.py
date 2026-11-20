from ..tasse import Tasse


class Cafe(Tasse):
    def __init__(self, prix: int, numero: list):
        super().__init__("Cafe", 2, [3])

    def effet(self, joueur,joueur_p, liste_joueurs, banque, reserve):
        joueur.payer(joueur_p,1)