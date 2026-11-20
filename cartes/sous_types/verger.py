from ..blé import Ble


class Verger(Ble):
    def __init__(self):
        super().__init__("Verger", 3, [10])

    def effet(self, joueur, liste_joueurs, banque, reserve):
        pass
