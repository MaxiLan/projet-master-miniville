import random
import time


class Joueur:
    def __init__(self, id: int):
        self._id = id
        self.monuments = []
        self.cartes = []
        self.piece_1 = 0
        self.piece_5 = 0
        self.piece_10 = 0

    @property
    def id(self):
        return self._id

    @property
    def argent(self):
        return self.piece_1 + 5 * self.piece_5 + 10 * self.piece_10

    def recevoir(self, somme: list):
        self.piece_1 += somme[0]
        self.piece_5 += somme[1]
        self.piece_10 += somme[2]

    def payer(self, joueur, somme: int):
        p10 = somme // 10
        p10 = min(p10, self.piece_10)
        reste = somme - 10 * p10

        p5 = reste // 5
        p5 = min(p5, self.piece_5)
        reste = reste - 5 * p5

        p1 = reste
        p1 = min(p1, self.piece_1)
        reste = reste - p1

        self.piece_10 -= p10
        self.piece_5 -= p5
        self.piece_1 -= p1

        joueur.recevoir([p1, p5, p10])
        return somme - reste  # on renvoie le vrai montant payé

    def ajouter_carte(self, carte):
        self.cartes.append(carte)

    def etat(self):
        print("Voici votre état")
        print(f"Argent : {self.argent}")

        s = ""
        for monument in self.monuments:
            construit = "" if monument.est_construit else "pas "
            s += f"{monument.nom} ({construit}construit); "

        print(f"Monuments : {s}")

        s = ""
        for carte in self.cartes:
            s += f"{carte.nom}; "
        print(f"Cartes : {s}")

    def lancer(self):
        de = 0
        nb_des = 1

        for monument in self.monuments:
            if monument.nom == "Gare" and monument.est_construit:
                nb_des = 2

        if nb_des == 2:
            if input("(Gare) Vous avez 2 dés. Voulez-vous lancer les 2 ? [y/n]") == "y":
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

        return de

    def tour(self, banque, reserve, joueurs_restants):
        """Réalise un tour du joueur"""
        de = self.lancer()

        # la tour radio permet de relancer les dés
        for monument in self.monuments:
            if monument.nom == "Tour radio" and monument.est_construit:
                if input("(Tour radio) Voulez-vous relancer vos dés ? [y/n]") == "y":
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

        return de

    def dessine(self):
        pass
