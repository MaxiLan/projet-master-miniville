from ..tasse import Tasse


class Cafe(Tasse):
    def __init__(self):
        super().__init__("Cafe", 2, [3])

    def effet(self, joueur, liste_joueurs, banque, reserve):
        banque.payer(joueur, 1)
