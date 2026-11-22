from cartes.carte import Carte


class Roue(Carte):
    def __init__(self, nom: str, prix: int, numeros: list):
        super().__init__(nom, "Roue", prix, numeros)
