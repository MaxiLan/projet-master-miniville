from spécial import Special


class Chaine_de_television(Special):
    def __init__(self):
        super().__init__("Chaine de télévision", 7, [6])

    def effet(self, joueur, liste_joueurs, banque, reserve):
        banque.payer(joueur, 1)
