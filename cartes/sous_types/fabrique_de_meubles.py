from ..usine import Usine


class Fabrique_de_meubles(Usine):
    def __init__(self):
        super().__init__("Fabrique de meubles", 3, [8])

    def effet(self, joueur, liste_joueurs, banque, reserve):
        pass
