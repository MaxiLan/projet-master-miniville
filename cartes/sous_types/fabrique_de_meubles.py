from ..usine import Usine


class Fabrique_de_meubles(Usine):
    def __init__(self):
        super().__init__("Fabrique de meubles", 3, [8])

    def effet(self, joueur_t, joueur_p, liste_joueurs, banque, reserve):
        for carte in joueur_p.liste_cartes:
            if carte.type == "Roue":
                banque.payer(joueur_p, 3)
