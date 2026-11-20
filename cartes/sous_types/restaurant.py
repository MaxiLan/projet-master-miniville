from ..tasse import Tasse


class Restaurant(Tasse):
    def __init__(self, prix: int, numero: list):
        super().__init__("Restaurant", 3, [9, 10])
    def effet(self, joueur, joueur_p, liste_joueurs, banque, reserve):
        #joueur qui lance dé donne 2 pièces
        if joueur._tour.nom==joueur.nom:
            for y in joueur._liste_cartes:
                if y.nom=="Restaurant":
                    joueur.payer(joueur_p, 2)