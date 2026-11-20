import random
#Classe dé
#que mettre dans l'init ? Méthode à ajouter ?
class De:
    def __init__(self):
        pass

    def lancer(self,joueur):
        d=[]
        if joueur.nb_de==2:
            d.append(random.randint(1, 6))
            d.append(random.randint(1, 6))
        d.append(random.randint(1, 6))
        return d
    