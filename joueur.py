import copy
import random
import time


class Joueur:
    def __init__(self, id: int):
        self._id = id
        self.monuments = []
        self.cartes = []
        self.argent = 0

    @property
    def id(self):
        return self._id

    def recevoir(self, somme: int):
        self.argent += somme

    def payer(self, entite, somme: int):
        """Le joueur paye la banque ou un joueur
        -entite: désigne la banque ou un autre joueur
        -somme: somme à payer
        """
        q = min(somme, self.argent)
        self.argent -= q
        entite.recevoir(q)
        return q  # on renvoie le vrai montant payé

    def ajouter_carte(self, carte):
        self.cartes.append(carte)

    def etat(self):
        print("Voici votre état")
        print(f"<Argent> : {self.argent}")

        s = ""
        for monument in self.monuments:
            construit = "" if monument.est_construit else "pas "
            s += f"{monument.nom} {monument.prix}$ ({construit}construit); "

        print(f"<Monuments> : {s}")

        s = ""
        for carte in self.cartes:
            s += f"{carte.nom}; "
        print(f"<Cartes> : {s}")

    def lancer(self):
        de = 0
        nb_des = 1
        print("\n")

        for monument in self.monuments:
            if monument.nom == "Gare" and monument.est_construit:
                nb_des = 2

        if nb_des == 2:
            if (
                input("(Gare) Vous avez 2 dés. Voulez-vous lancer les deux ? [y/n] ")
                == "y"
            ):
                print("Vous lancez 2 dés...")
                time.sleep(1)
                de1 = random.randint(1, 6)
                print(f"Le premier lancer donne {de1}")
                de2 = random.randint(1, 6)
                print(f"Le deuxième lancer donne {de2}")
                de = de1 + de2
                print(f"Le total est donc {de}")
            else:
                print("Vous lancez un dé...")
                time.sleep(1)
                de = random.randint(1, 6)
                print(f"Le résultat est {de}")
        else:
            print("Vous lancez un dé...")
            time.sleep(1)
            de = random.randint(1, 6)
            print(f"Le résultat est {de}")

        return de

    def tour(self, banque, reserve, joueurs_restants):
        """Réalise un tour du joueur"""
        de = self.lancer()

        # la tour radio permet de relancer les dés
        for monument in self.monuments:
            if monument.nom == "Tour radio" and monument.est_construit:
                if input("(Tour radio) Voulez-vous relancer vos dés ? [y/n] ") == "y":
                    de = self.lancer()
                    break

        # active les effets des cartes du joueur
        for carte in self.cartes:
            if de in carte.numeros:
                carte.effet(self, self, joueurs_restants, banque, reserve)

        # regarder chez les autres joueurs si l'effet est activable
        for j in joueurs_restants:
            for carte in j.cartes:
                if de in carte.numeros and carte.activable:
                    carte.effet(self, j, joueurs_restants, banque, reserve)

        # choix des monuments/cartes
        continuer = True

        while (
            continuer
            and input("Voulez-vous construire un de vos monuments ? [y/n] ") == "y"
        ):
            nom = input("Entrez le choix du monument (nom du monument) : ")
            cpt = 0
            for monument in self.monuments:
                if nom == monument.nom:
                    if self.argent >= monument.prix:
                        monument.est_construit = True
                        self.payer(banque, monument.prix)
                        print(f"Vous avez construit le monument : {nom}")
                        continuer = False
                        break
                    else:
                        print("Vous n'avez pas assez d'argent")
                        break
                cpt += 1
            if cpt == 4:
                print("Ce monument n'existe pas")

        while continuer and input("Voulez-vous acheter un bâtiment ? [y/n] ") == "y":
            reserve.etat()
            print("\n")
            nom = input("Entrez le choix du bâtiment (nom de la carte) : ")
            cpt = 0
            for carte in reserve.cartes:
                if nom == carte[0].nom:
                    if self.argent >= carte[0].prix:
                        if carte[1] > 0:
                            self.payer(banque, carte[0].prix)
                            carte[1] -= 1
                            # on ajoute une copie de la carte au joueur
                            self.ajouter_carte(copy.deepcopy(carte[0]))
                            print(f"Vous avez acheté le bâtiment : {nom}")
                            continuer = False
                            break
                        else:
                            print("Cette carte est épuisée")
                            break
                    else:
                        print("Vous n'avez pas assez d'argent")
                        break
                cpt += 1
            if cpt == len(reserve.cartes):
                print("Ce bâtiment n'existe pas")

        return de  # renvoie la valeur du dé pour savoir si le joueur rejoue

    def dessine(self):
        pass
