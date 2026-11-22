from cartes.sous_types.monument import Monument


class Parc_d_attractions(Monument):
    def __init__(self):
        super().__init__("Parc d'attractions", 16)

    def effet(self, joueur_t, joueur_p, liste_joueurs, banque, reserve):
        if joueur.nb_de == 2:
            if de.lancer[0] == de.lancer[1]:
                joueur.relancer(True)
