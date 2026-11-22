from cartes.brioche import Brioche


class Superette(Brioche):
    def __init__(self):
        super().__init__("Superette", 4, [4])

    def effet(self, joueur_t, joueur_p, liste_joueurs, banque, reserve):
        for monument in joueur_p:
            if monument.nom == "Centre commercial" and monument.est_construit:
                banque.payer(joueur_p, 4)
            else:
                banque.payer(joueur_p, 3)
            break
