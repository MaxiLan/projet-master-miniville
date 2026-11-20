from ..brioche import Brioche


# faire une liste avec les joeurs de la partie,
# en faire un attribut dans cette classe,
# et trouver dans cette liste le joueur qui joue, pour lui verser l'argent ?
class Boulangerie(Brioche):
    def __init__(self, prix: int, numero: list):
        super().__init__("Boulangerie", 1, [2, 3])

    def effet(self, joueur, joueur_p, liste_joueurs, banque, reserve):
        for y in joueur._liste_cartes:
            if y.nom=="Boulangerie":
                banque.payer(joueur, 1)
