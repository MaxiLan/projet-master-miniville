from cartes.tasse import Tasse


class Cafe(Tasse):
    def __init__(self):
        super().__init__("Café", 2, [3])
        self._activable = True

    def effet(self, joueur_t, joueur_p, liste_joueurs, banque, reserve):
        for monument in joueur_p.monuments:
            if monument.nom == "Centre commercial":
                if monument.est_construit:
                    res = joueur_t.payer(joueur_p, 2)
                    print(f"({self.nom}) Vous donnez {res}$ au joueur {joueur_p.id+1}")
                    break
                else:
                    res = joueur_t.payer(joueur_p, 1)
                    print(f"({self.nom}) Vous donnez {res}$ au joueur {joueur_p.id+1}")
                    break
