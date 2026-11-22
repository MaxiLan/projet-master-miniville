from cartes.brioche import Brioche


class Boulangerie(Brioche):
    def __init__(self):
        super().__init__("Boulangerie", 1, [2, 3])

    def effet(self, joueur_t, joueur_p, liste_joueurs, banque, reserve):
        for monument in joueur_p.monuments:
            if monument.nom == "Centre commercial" and monument.est_construit:
                res = banque.payer(joueur_p, 2)
                print(f"(Boulangerie) La banque vous donne {res}")
            else:
                res = banque.payer(joueur_p, 1)
                print(f"(Boulangerie) La banque vous donne {res}")
            break
