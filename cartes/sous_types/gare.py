from cartes.sous_types.monument import Monument


class Gare(Monument):
    def __init__(self):
        super().__init__("Gare", 4)
        self.est_construit=True

    def effet(self, joueur_t, joueur_p, liste_joueurs, banque, reserve):
        for joueur in liste_joueurs:
            for carte in joueur.liste_cartes:
                if carte.nom == "Gare":
                    joueur.nb_de = 2
