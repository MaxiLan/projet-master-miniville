from monument import Monument


class Gare(Monument):
    def __init__(self, prix):
        super().__init__("Gare", 4)

    def effet(self, joueur, liste_joueurs, banque, reserve):
        for x in liste_joueurs:
            for y in x._liste_cartes:
                if y.nom="Gare":
                    x.nb_de=2