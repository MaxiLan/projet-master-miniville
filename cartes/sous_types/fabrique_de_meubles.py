from ..usine import Usine


class Fabrique_de_meubles(Usine):
    def __init__(self, prix: int, numero: list):
        super().__init__("Fabrique de meubles", 3, [8])

    def effet(self, joueur,joueur_p,liste_joueurs, banque, reserve):
        for x in joueur._liste_cartes:
            if x.typ=="Roue":
                banque.payer(joueur,3)