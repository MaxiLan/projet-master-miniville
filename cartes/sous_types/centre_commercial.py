from monument import Monument


class Centre_commercial(Monument):
    def __init__(self, prix: int):
        super().__init__("Centre commercial", 10)

    def effet(self, joueur, liste_joueurs, banque, reserve):
        for x in liste_joueurs:
            for y in x._liste_cartes:
                if y.typ=="Tasse" or y.typ=="Brioche":
                    banque.payer(x,1)