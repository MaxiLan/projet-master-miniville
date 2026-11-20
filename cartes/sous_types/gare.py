from monument import Monument


class Gare(Monument):
    def __init__(self):
        super().__init__("Gare", 4)

    def effet(self, joueur, liste_joueurs, banque, reserve):
        pass
