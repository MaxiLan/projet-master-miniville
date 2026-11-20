from ..brioche import Brioche


class Superette(Brioche):
    def __init__(self):
        super().__init__("Superette", 4, [4])

    def effet(self, joueur_t, joueur_p, liste_joueurs, banque, reserve):
        # pdt son tour, le joueur reçoit 3 pièces de la banque
        banque.payer(joueur_p, 3)
