from cartes.tasse import Tasse


class Restaurant(Tasse):
    def __init__(self):
        super().__init__("Restaurant", 3, [9, 10])

    def effet(self, joueur_t, joueur_p, liste_joueurs, banque, reserve):
        for monument in joueur_p:
            if monument.nom == "Centre commercial" and monument.est_construit:
                joueur_t.payer(joueur_p, 3)
            else:
                joueur_t.payer(joueur_p, 2)
            break
