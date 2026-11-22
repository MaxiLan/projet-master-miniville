class Banque:
    def __init__(self):
        self.piece_1 = 36
        self.piece_5 = 9
        self.piece_10 = 9

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
        reste = reste - p1

        self.piece_10 -= p10
        self.piece_5 -= p5
        self.piece_1 -= p1

        joueur.recevoir([p1, p5, p10])
        return somme - reste  # on renvoie le vrai montant payé
