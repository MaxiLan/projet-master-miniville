from spécial import Special


class Chaine_de_television(Special):
    def __init__(self, prix: int, numero: list):
        super().__init__("Chaine de télévision", 7, [6])

    def effet(self, joueur,joueur_p, liste_joueurs, banque, reserve):
        #pareil, comment choisir le joueur qui va nous donner la thune ?