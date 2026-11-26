from cartes.sous_types.boulangerie import Boulangerie
from cartes.sous_types.cafe import Cafe
from cartes.sous_types.centre_d_affaires import Centre_d_affaires
from cartes.sous_types.chaine_de_television import Chaine_de_television
from cartes.sous_types.champs_de_ble import Champs_de_ble
from cartes.sous_types.fabrique_de_meubles import Fabrique_de_meubles
from cartes.sous_types.ferme import Ferme
from cartes.sous_types.foret import Foret
from cartes.sous_types.fromagerie import Fromagerie
from cartes.sous_types.marche_de_legumes import Marche_de_legumes
from cartes.sous_types.mine import Mine
from cartes.sous_types.restaurant import Restaurant
from cartes.sous_types.stade import Stade
from cartes.sous_types.superette import Superette
from cartes.sous_types.verger import Verger


class Reserve:
    def __init__(self):
        # effectif de chaque carte dans la pioche/réserve
        self.cartes = [
            [Champs_de_ble(), 6],
            [Ferme(), 6],
            [Boulangerie(), 6],
            [Cafe(), 6],
            [Superette(), 6],
            [Foret(), 6],
            [Centre_d_affaires(), 4],
            [Stade(), 4],
            [Chaine_de_television(), 4],
            [Fromagerie(), 6],
            [Fabrique_de_meubles(), 6],
            [Mine(), 6],
            [Restaurant(), 6],
            [Verger(), 6],
            [Marche_de_legumes(), 6],
        ]

    def etat(self):
        print("Cartes de la réserve :")
        s = ""
        for carte in self.cartes:
            s += f"- [{carte[1]}] {carte[0].nom} ${carte[0].prix};\n"
        print(s)

    def dessine(self):
        pass
