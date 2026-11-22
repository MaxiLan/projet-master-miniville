from cartes.sous_types.monument import Monument


class Centre_commercial(Monument):
    def __init__(self):
        super().__init__("Centre commercial", 10)

    def effet(self, joueur_t, joueur_p, liste_joueurs, banque, reserve):
        for y in joueur_p.liste_cartes:
            if y.typ == "Tasse" or y.typ == "Brioche":
                banque.payer(joueur_p, 1)
