from ..vache import Vache


class Ferme(Vache):
    def __init__(self):
        super().__init__("Ferme", 1, [2])

    def effet(self, joueur_t, joueur_p, liste_joueurs, banque, reserve):
        banque.payer(joueur_p, 1)
