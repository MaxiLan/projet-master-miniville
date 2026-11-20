from monument import Monument


class Tour_radio(Monument):
    def __init__(self, prix: int):
        super().__init__("Tour radio", 22)

    def effet(self, c:bool, joueur, joueur_p, liste_joueurs, banque, reserve):
        if joueur._tour.nom==joueur.nom:
            joueur.relancer(c)

#On choisit de relancer ou non avec c