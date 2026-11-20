from ..tasse import Tasse


class Restaurant(Tasse):
    def __init__(self):
        super().__init__("Restaurant", 3, [9, 10])

    def effet(self, joueur_t, joueur_p, liste_joueurs, banque, reserve):
        # joueur qui lance dé donne 2 pièces
        # Regarder dans la liste des joueurs, qui joue : joueur2
        joueur_t.payer(joueur_p, 2)
