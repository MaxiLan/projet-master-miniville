from ..usine import Usine


class Fromagerie(Usine):
    def __init__(self, prix: int, numero: list):
        super().__init__("Fromagerie", 5, [7])

    def effet(self, joueur, liste_joueurs, banque, reserve):
        for x in joueur._liste_cartes:
            if x.typ=="Vache":
                banque.payer(joueur,3)