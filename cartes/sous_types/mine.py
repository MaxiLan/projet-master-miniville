from ..roue import Roue


class Mine(Roue):
    def __init__(self, prix: int, numero: list):
        super().__init__("Mine", 6, [9])
    def effet(self, joueur, joueur_p, liste_joueurs, banque, reserve):
        #à chaque tour, banque paye 5 pièces
        for y in joueur._listes_cartes:
            if y.nom=="Mine"
                banque.payer(joueur,5)
