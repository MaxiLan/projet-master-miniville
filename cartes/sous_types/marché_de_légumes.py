from ..tomate import Tomate


class Marche_de_legumes(Tomate):
    def __init__(self):
        super().__init__("Marché de légumes", 2, [11, 12])

    def effet(self, joueur, liste_joueurs, banque, reserve):
        pass
