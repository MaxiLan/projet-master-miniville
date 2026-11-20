from ..tasse import Tasse


class Restaurant(Tasse):
    def __init__(self):
        super().__init__("Restaurant", 3, [9, 10])

    def effet(self, joueur, liste_joueurs, banque, reserve):
        pass
