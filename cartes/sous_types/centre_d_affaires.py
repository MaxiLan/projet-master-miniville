from cartes.sous_types.special import Special


class Centre_d_affaires(Special):
    def __init__(self):
        super().__init__("Centre d'affaires", 8, [6])

    def effet(self, joueur_t, joueur_p, liste_joueurs, banque, reserve):
        choix = input(
            f"({self.nom}) Voulez-vous échanger une carte avec un autre joueur ? [y/n] : "
        )
        if choix != "y":
            return

        choix = liste_joueurs[0].id
        choix_valides = [j.id for j in liste_joueurs]
        continuer = True
        while continuer:
            choix = input(
                "Choisissez un joueur avec qui échanger une carte (son numéro) : "
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

        print(f"Le joueur {choix+1} a comme cartes à échanger :")
        for carte in choix_joueur.cartes:
            print(f"- {carte.nom}")

        continuer = True
        cpt = 0
        while continuer:
            choix = input("Entrez votre choix (nom de la carte) : ")
            for i in range(len(choix_joueur.cartes)):
                if choix_joueur.cartes[i].nom == choix:
                    # échange
                    joueur_p.ajouter_carte(choix_joueur.cartes[i])
                    del choix_joueur.cartes[i]
                    continuer = False
                    break
                cpt += 1

            if cpt == len(choix_joueur.cartes):
                print("Cette carte n'existe pas")
