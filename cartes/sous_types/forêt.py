from ..roue import Roue


class Foret(Roue):
    def __init__(self):
        super().__init__("Roue", 3, [5])

    def effet(self, joueur_t, joueur_p, liste_joueurs, banque, reserve):
        banque.payer(joueur_p, 1)
