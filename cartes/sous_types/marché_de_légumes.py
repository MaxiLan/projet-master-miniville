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

