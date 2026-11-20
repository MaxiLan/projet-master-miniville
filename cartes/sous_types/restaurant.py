from ..tasse import Tasse


class Restaurant(Tasse):
    def __init__(self, prix: int, numero: list):
        super().__init__("Restaurant", 3, [9, 10])
    def effet(self, joueur, liste_joueurs, banque, reserve):
        #joueur qui lance dé donne 2 pièces
        #Regarder dans la liste des joueurs, qui joue : joueur2
        joueur2.payer(joueur, 2)
        joueur.recevoir(2)