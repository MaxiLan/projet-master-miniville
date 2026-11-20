from spécial import Special


class Centre_d_affaires(Special):
    def __init__(self, prix: int, numero: list):
        super().__init__("Centre d'affaires", 8, [6])

    def effet(self, joueur, liste_joueurs, banque, reserve):
        #faire une méthode pour savoir qui joue ?