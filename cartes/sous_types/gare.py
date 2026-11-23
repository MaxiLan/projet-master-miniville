from cartes.sous_types.monument import Monument


class Gare(Monument):
    def __init__(self):
        super().__init__("Gare", 4)

    def effet(self, joueur_t, joueur_p, liste_joueurs, banque, reserve):
        #for monument in joueur_p.monuments:
        #    if monument.nom == "Gare" and self.est_construit==True:
        #        joueur_p.nb_de = 2
        pass
    #ici, effet déjà mis dans joueur : méthode lancer