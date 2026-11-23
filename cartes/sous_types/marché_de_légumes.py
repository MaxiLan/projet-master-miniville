from cartes.tomate import Tomate


class Marche_de_legumes(Tomate):
    def __init__(self):
        super().__init__("Marché de fruits et légumes", 2, [11, 12])

    def effet(self, joueur_t, joueur_p, liste_joueurs, banque, reserve):
        # Pendant le tour du joueur, la banque paye 2*nbr d'établissements blé que le joueur possède
        s = 0
        for carte in joueur_p.cartes:
            if carte.type == "Blé":
                s += 2
        banque.payer(joueur_p, s)


# car si dans la classe Jeu, on active les effets
# en fonction des listes de carte de chaque joueur,
# alors on sait deja que la carte est dans le liste
# de cartes du joueur ?
# Autre pb, si l'effet s'applique à chaque tour, même
# quand ce n'est pas le tour du joueur ?
# On pourrait ne pas mettre celui à qui c'est le tour dans
# les attributs, mais plutot de faire une méthode comme
# dit avec le premier if ?
