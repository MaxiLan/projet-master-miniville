from cartes.roue import Roue


class Foret(Roue):
    def __init__(self):
        super().__init__("Forêt", 3, [5])
        self._activable = True

    def effet(self, joueur_t, joueur_p, liste_joueurs, banque, reserve):
        banque.payer(joueur_p, 1)
