from cartes.sous_types.spécial import Special


class Stade(Special):
    def __init__(self):
        super().__init__("Stade", 6, [6])

    def effet(self, joueur_t, joueur_p, liste_joueurs, banque, reserve):
        for joueur in liste_joueurs:
            joueur.payer(joueur_p, 2)
