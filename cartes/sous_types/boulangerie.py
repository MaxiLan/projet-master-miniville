from ..brioche import Brioche


# Sous-sous classe Boulangerie
# faire une liste avec les joeurs de la partie,
# en faire un attribut dans cette classe,
# et trouver dans cette liste le joueur qui joue, pour lui verser l'argent ?
class Boulangerie(Brioche):
    def __init__(self, prix: int, numero: list):
        super().__init__("Boulangerie", 1, [2, 3])
