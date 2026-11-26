from cartes.sous_types.special import Special


class Chaine_de_television(Special):
    def __init__(self):
        super().__init__("Chaine de télévision", 7, [6])

    def effet(self, joueur_t, joueur_p, liste_joueurs, banque, reserve):
        choix = liste_joueurs[0].id
        choix_valides = [j.id for j in liste_joueurs]
        continuer = True
        while continuer:
            choix = input(
                f"({self.nom}) Choisissez un joueur qui vous paierai 5$ (son numéro) : "
            )
            choix = int(choix) - 1
            if choix in choix_valides:
                continuer = False
                break
            print("Ce numéro n'est pas valide")

        choix_joueur = liste_joueurs[0]
        for j in liste_joueurs:
            if j.id == choix:
                choix_joueur = j
                break

        res = choix_joueur.payer(joueur_p, 5)
        print(f"Le joueur {choix+1} vous donne {res}$")
