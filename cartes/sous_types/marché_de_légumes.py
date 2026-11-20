from ..tomate import Tomate


class Marche_de_legumes(Tomate):
    def __init__(self):
        super().__init__("Marché de légumes", 2, [11, 12])

    def effet(self, joueur_t, joueur_p, liste_joueurs, banque, reserve):
        pass
        # Pendant le tour du joueur, la banque paye 2*nbr d'établissements blé que le joueur possède
        # Regarder quel joueur joue
        # Trouver le joueur dans la liste des joueurs
        # Regarder dans la liste des cartes du joueur cb de cartes blé il possède
        # banque.payer(joueur_p, 2*nbr blé)
