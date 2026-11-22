from cartes.blé import Ble


class Champs_de_ble(Ble):
    def __init__(self):
        super().__init__("Champs de blé", 1, [1])
        self._activable = True

    def effet(self, joueur_t, joueur_p, liste_joueurs, banque, reserve):
        res = banque.payer(joueur_p, 1)
        print(f"[Joueur {joueur_p.id+1}] (Champs de blé) La banque vous donne {res}")
