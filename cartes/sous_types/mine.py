from cartes.roue import Roue


class Mine(Roue):
    def __init__(self):
        super().__init__("Mine", 6, [9])
        self._activable = True

    def effet(self, joueur_t, joueur_p, liste_joueurs, banque, reserve):
        # à chaque tour, banque paye 5 pièces
        res = banque.payer(joueur_p, 5)
        print(f"[Joueur {joueur_p.id+1}] (Mine) La banque vous donne {res}")
