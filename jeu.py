import time

from banque import Banque
from cartes.sous_types.boulangerie import Boulangerie
from cartes.sous_types.centre_commercial import Centre_commercial
from cartes.sous_types.centre_d_affaires import Centre_d_affaires
from cartes.sous_types.chaine_de_television import Chaine_de_television
from cartes.sous_types.champs_de_ble import Champs_de_ble
from cartes.sous_types.fabrique_de_meubles import Fabrique_de_meubles
from cartes.sous_types.ferme import Ferme
from cartes.sous_types.foret import Foret
from cartes.sous_types.fromagerie import Fromagerie
from cartes.sous_types.gare import Gare
from cartes.sous_types.marche_de_legumes import Marche_de_legumes
from cartes.sous_types.mine import Mine
from cartes.sous_types.parc_d_attractions import Parc_d_attractions
from cartes.sous_types.restaurant import Restaurant
from cartes.sous_types.stade import Stade
from cartes.sous_types.superette import Superette
from cartes.sous_types.tour_radio import Tour_radio
from cartes.sous_types.verger import Verger
from joueur import Joueur
from reserve import Reserve


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
            joueur.cartes = [
                Champs_de_ble(),
                Boulangerie(),
                Mine(),  # pour tester
                Restaurant(),
                Stade(),
                Superette(),
                Tour_radio(),
                Verger(),
                Fromagerie(),
                Marche_de_legumes(),
                Chaine_de_television(),
                Fabrique_de_meubles(),
                Foret(),
                Ferme(),
                Centre_d_affaires(),
            ]
            self.joueurs.append(joueur)

    def jouer(self):
        """Réalise un tour de jeu"""
        joueur = self.joueurs[self.joueur_courant]
        joueurs_restants = [j for j in self.joueurs if j.id != self.joueur_courant]

        print(f"----------Le joueur {self.joueur_courant+1} joue son tour----------")
        time.sleep(1)
        joueur.etat()
        time.sleep(1)
        double = joueur.tour(self.banque, self.reserve, joueurs_restants)

        # le joueur rejoue avec le parc d'attractions
        if double:
            for monument in joueur.monuments:
                if monument.nom == "Parc d'attractions" and monument.est_construit:
                    print("(Parc d'attractions) Vous rejouez !")
                    joueur.tour(self.banque, self.reserve, joueurs_restants)
                    break

        input("> Continuer [entrée] <")

        self.est_fini = all([monument.est_construit for monument in joueur.monuments])
        if self.est_fini:
            print(f"Le joueur {self.joueur_courant+1} a gagné !")
        self.joueur_courant = (self.joueur_courant + 1) % self.nb_joueurs
