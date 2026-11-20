from ..brioche import Brioche


class Superette(Brioche):
    def __init__(self):
        super().__init__("Superette", 4, [4])

    def effet(self, joueur, liste_joueurs, banque, reserve):
        pass
