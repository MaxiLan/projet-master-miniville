from ..antenne import Antenne


class Monument(Antenne):  # classe abstraite
    def __init__(self, nom: str, prix: int):
        super().__init__(nom, prix, [])

