from cartes.tomate import Tomate


class Marche_de_legumes(Tomate):
    def __init__(self, prix: int, numero: list):
        super().__init__("Marché de légumes", 2, [11, 12])

    def effet(self, joueur, joueur_p, liste_joueurs, banque, reserve):
        # Pendant le tour du joueur, la banque paye 2*nbr d'établissements blé que le joueur possède
        if (
            joueur._tour.nom == joueur.nom
        ):  # Methode dans jeu pour savoir à qui c'est le tour
            for y in joueur._listes_cartes:  # est-ce obligé de mettre ça ? *
                k = 0
                if y.type == Ble:
                    k += 1
            banque.payer(joueur_p, 2 * k)


# car si dans la classe Jeu, on active les effets
# en fonction des listes de carte de chaque joueur,
# alors on sait deja que la carte est dans le liste
# de cartes du joueur ?
# Autre pb, si l'effet s'applique à chaque tour, même
# quand ce n'est pas le tour du joueur ?
# On pourrait ne pas mettre celui à qui c'est le tour dans
# les attributs, mais plutot de faire une méthode comme
# dit avec le premier if ?
