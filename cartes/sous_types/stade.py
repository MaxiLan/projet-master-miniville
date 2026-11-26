from cartes.sous_types.special import Special


class Stade(Special):
    def __init__(self):
        super().__init__("Stade", 6, [6])

    def effet(self, joueur_t, joueur_p, liste_joueurs, banque, reserve):
        res = 0
        for joueur in liste_joueurs:
            res += joueur.payer(joueur_p, 2)
        print(f"({self.nom}) Les autres joueurs vous donnent au total {res}$")
