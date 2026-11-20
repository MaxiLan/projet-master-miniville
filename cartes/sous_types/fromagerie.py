from ..usine import Usine


class Fromagerie(Usine):
    def __init__(self):
        super().__init__("Fromagerie", 5, [7])

    def effet(self, joueur_t, joueur_p, liste_joueurs, banque, reserve):
        for carte in joueur_p.liste_cartes:
            if carte.type == "Vache":
                banque.payer(joueur_p, 3)
