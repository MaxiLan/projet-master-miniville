from cartes.sous_types.spécial import Special


class Stade(Special):
    def __init__(self, prix: int, numero: list):
        super().__init__("Stade", 6, [6])

    def effet(self, joueur, joueur_p, liste_joueurs, banque, reserve):
        # pdt son tour, le joueur recoit 2 pieces de tous les autres joueurs
        if joueur._tour.nom == joueur.nom:
            for y in joueur._liste_cartes:
                if y.nom == "Stade":
                    for x in liste_joueurs:
                        x.payer(joueur, 2)
