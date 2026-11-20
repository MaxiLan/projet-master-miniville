from ..tasse import Tasse


class Cafe(Tasse):
    def __init__(self):
        super().__init__("Cafe", 2, [3])

    def effet(self, joueur_t, joueur_p, liste_joueurs, banque, reserve):
        joueur_t.payer(joueur_p, 1)
