from ..blé import Ble


class Verger(Ble):
    def __init__(self, prix: int, numero: list):
        super().__init__("Verger", 3, [10])
    def effet(self, joueur, liste_joueurs, banque, reserve):
        #à chaque tour, le joueur reçoit 3 de la banque 
        banque.payer(joueur, 3)
