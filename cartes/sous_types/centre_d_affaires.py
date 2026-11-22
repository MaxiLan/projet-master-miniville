from cartes.sous_types.spécial import Special


class Centre_d_affaires(Special):
    def __init__(self):
        super().__init__("Centre d'affaires", 8, [6])

    def effet(self, joueur_t, joueur_p, liste_joueurs, banque, reserve):
        for carte in joueur_p.liste_cartes:
            pass
            # comment choisir un autre joueur ? au hasard?
            # ajout de joueur_c : joueur choisi :
            # demander de rentrer le nom du joueur choisi ?
