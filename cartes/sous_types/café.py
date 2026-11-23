from cartes.tasse import Tasse


class Cafe(Tasse):
    def __init__(self):
        super().__init__("Café", 2, [3])

    def effet(self, joueur_t, joueur_p, liste_joueurs, banque, reserve):
        for monument in joueur_p.monuments:
            if monument.nom == "Centre commercial" and monument.est_construit:
                joueur_t.payer(joueur_p, 2)
            else:
                joueur_t.payer(joueur_p, 1)
            break
