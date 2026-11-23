from cartes.blé import Ble


class Verger(Ble):
    def __init__(self):
        super().__init__("Verger", 3, [10])
        self._activable = True

    def effet(self, joueur_t, joueur_p, liste_joueurs, banque, reserve):
        # à chaque tour, le joueur reçoit 3 de la banque
        res = banque.payer(joueur_p, 3)
        print(f"[Joueur {joueur_p.id+1}] (Verger) La banque vous donne {res}")
