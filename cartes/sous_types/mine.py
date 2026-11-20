from ..roue import Roue


class Mine(Roue):
    def __init__(self):
        super().__init__("Mine", 6, [9])

    def effet(self, joueur_t, joueur_p, liste_joueurs, banque, reserve):
        # à chaque tour, banque paye 5 pièces
        banque.payer(joueur_p, 5)
