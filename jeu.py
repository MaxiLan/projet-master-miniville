import time

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
            joueur.monuments = [
                Gare(),
                Centre_commercial(),
                Tour_radio(),
                Parc_d_attractions(),
            ]
            joueur.cartes = [Champs_de_ble(), Boulangerie()]
            self.joueurs.append(joueur)

    def jouer(self):
        """Réalise un tour de jeu"""
        joueur = self.joueurs[self.joueur_courant]
        joueurs_restants = [j for j in self.joueurs if j.id != self.joueur_courant]

        print(f"----------Le joueur {self.joueur_courant+1} joue son tour----------")
        time.sleep(1)
        joueur.etat()

        de = joueur.tour(self.banque, self.reserve, joueurs_restants)

        # le joueur rejoue avec le parc d'attractions
        if de % 2 == 0:
            for monument in joueur.monuments:
                if monument.nom == "Parc d'attractions" and monument.est_construit:
                    print("(Parc d'attractions) Vous rejouez !")
                    joueur.tour(self.banque, self.reserve, joueurs_restants)
                    break

        input("> Continuer [entrée] <")

        self.est_fini = all([monument.est_construit for monument in joueur.monuments])
        self.joueur_courant = (self.joueur_courant + 1) % self.nb_joueurs
