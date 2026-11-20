class Joueur:
    def __init__(self, nom: str, argent: int):
        self._nom = nom
        self._argent = 3
        self._liste_cartes = []
        self._nb_de=1

    @property
    def nb_de(self):
        return self._nb_de

    def agir(self):
        n = de.lancer()

    def recevoir(self, somme: int):
        self._argent += somme

    def payer(self, joueur, somme: int):
        if self._argent <= somme:
            joueur.recevoir(self._argent)
            self._argent = 0

        joueur.recevoir(somme)
        self._argent -= somme
