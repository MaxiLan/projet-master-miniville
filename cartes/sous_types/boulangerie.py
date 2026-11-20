from ..brioche import Brioche


# faire une liste avec les joeurs de la partie,
# en faire un attribut dans cette classe,
# et trouver dans cette liste le joueur qui joue, pour lui verser l'argent ?
class Boulangerie(Brioche):
    def __init__(self):
        super().__init__("Boulangerie", 1, [2, 3])

    def effet(self, joueur_t, joueur_p, liste_joueurs, banque, reserve):
        banque.payer(joueur_p, 1)
