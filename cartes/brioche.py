from carte import Carte


class Brioche(Carte):
    def __init__(self, nom: str, prix: int, numeros: list):
        super().__init__(nom, "Brioche", prix, numeros)
