from ..roue import Roue


class Mine(Roue):
    def __init__(self):
        super().__init__("Mine", 6, [9])

    def effet(self, joueur, liste_joueurs, banque, reserve):
        pass
