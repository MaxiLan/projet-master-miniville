from ..brioche import Brioche


class Superette(Brioche):
    def __init__(self, prix: int, numero: list):
        super().__init__("Superette", 4, [4])
    def effet(self, joueur, joueur_p, liste_joueurs, banque, reserve):
        #pdt son tour, le joueur reçoit 3 pièces de la banque
        if joueur._tour.nom==joueur.nom:
            banque.payer(joueur, 3)
