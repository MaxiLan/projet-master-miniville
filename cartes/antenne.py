from carte import Carte


class Antenne(Carte):
    def __init__(self, nom: str, prix: int, numeros: list):
        super().__init__(nom, "Antenne", prix, numeros)
