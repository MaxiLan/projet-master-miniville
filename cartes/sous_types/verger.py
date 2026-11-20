from ..blé import Ble


class Verger(Ble):
    def __init__(self, prix: int, numero: list):
        super().__init__("Verger", 3, [10])
    def effet(self, joueur, joueur_p, liste_joueurs, banque, reserve):
        banque.payer(joueur, 3)
