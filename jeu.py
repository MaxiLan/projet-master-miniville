import random

from banque import Banque
from cartes.sous_types.boulangerie import Boulangerie
from cartes.sous_types.centre_commercial import Centre_commercial
from cartes.sous_types.champs_de_blé import Champs_de_ble
from cartes.sous_types.gare import Gare
from cartes.sous_types.parc_d_attractions import Parc_d_attractions
from cartes.sous_types.tour_radio import Tour_radio
from joueur import Joueur
from réserve import Reserve


class Jeu:
    def __init__(self, nb_joueurs):
        self.banque = Banque()
        self.reserve = Reserve()
        self.nb_joueurs = nb_joueurs
        self.joueurs = []
        self.joueur_courant = 0  # id du joueur dont c'est le tour
        self.est_fini = False

        for i in range(nb_joueurs):
            joueur = Joueur(i)

            # argent de départ
            self.banque.payer(joueur, 3)

            # cartes de départ
            joueur.liste_cartes.append(
                Gare(),
                Centre_commercial(),
                Tour_radio(),
                Parc_d_attractions(),
                Champs_de_ble(),
                Boulangerie(),
            )
            self.joueurs.append(joueur)

    def jouer(self):
        joueur = self.joueurs[self.joueur_courant]
        joueurs_restants = [j for j in self.joueurs if j.id != self.joueur_courant]

        print(f"Le joueur {self.joueur_courant+1} lance son dé...")
        de = random.randint(1, 6)
        print(f"Le résultat est : {de}")

        for carte in joueur.liste_cartes:
            if de in carte.numeros:
                carte.effet(joueur, self.joueurs, self.banque, self.reserve)

        for j in joueurs_restants:
            for carte in j.liste_cartes:
                if de in carte.numeros:
                    carte.effet(joueur, self.joueurs, self.banque, self.reserve)
