from cartes.carte import Carte


class Ble(Carte):
    def __init__(self, nom: str, prix: int, numeros: list):
        super().__init__(nom, "Blé", prix, numeros)
