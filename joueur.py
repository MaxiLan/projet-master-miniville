class Joueur:
    def __init__(self, id: int):
        self._id = id
        self.liste_cartes = []
        self.piece_1 = 0
        self.piece_5 = 0
        self.piece_10 = 0

    @property
    def id(self):
        return self._id

    @property
    def argent(self):
        return self.piece_1 + 5 * self.piece_5 + 10 * self.piece_10

    def recevoir(self, somme: list):
        self.piece_1 += somme[0]
        self.piece_5 += somme[1]
        self.piece_10 += somme[2]

    def payer(self, joueur, somme: int):
        p10 = somme // 10
        p10 = min(p10, self.piece_10)
        reste = somme - 10 * p10

        p5 = reste // 5
        p5 = min(p5, self.piece_5)
        reste = reste - 5 * p5

        p1 = reste
        p1 = min(p1, self.piece_1)

        self.piece_10 -= p10
        self.piece_5 -= p5
        self.piece_1 -= p1

        joueur.recevoir([p1, p5, p10])

    def ajouter_carte(self, carte):
        self.liste_cartes.append(carte)

    def dessine(self):
        pass
