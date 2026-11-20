from spécial import Special


class Centre_d_affaires(Special):
    def __init__(self, prix: int, numero: list):
        super().__init__("Centre d'affaires", 8, [6])

    def effet(self, joueur, liste_joueurs, banque, reserve):
        for x in joueur._liste_cartes:
            #comment choisir un autre joueur ? au hasard?
            #ajout de joueur_c : joueur choisi : 
            #demander de rentrer le nom du joueur choisi ?
            