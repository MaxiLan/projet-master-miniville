from ..blé import Ble


class Champs_de_ble(Ble):
    def __init__(self, prix: int, numero: list):
        super().__init__("Champs de blé", 1, [1])

    def effet(self, joueur, liste_joueurs, banque, reserve):
        banque.payer(joueur, 1)