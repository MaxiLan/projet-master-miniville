from cartes.brioche import Brioche


class Superette(Brioche):
    def __init__(self):
        super().__init__("Supérette", 2, [4])

    def effet(self, joueur_t, joueur_p, liste_joueurs, banque, reserve):
        for monument in joueur_p.monuments:
            if monument.nom == "Centre commercial" and monument.est_construit:
                res = banque.payer(joueur_p, 4)
                print(
                    f"[Joueur {joueur_p.id+1}] (Supérette) La banque vous donne {res}"
                )
            else:
                res = banque.payer(joueur_p, 3)
                print(
                    f"[Joueur {joueur_p.id+1}] (Supérette) La banque vous donne {res}"
                )
            break
