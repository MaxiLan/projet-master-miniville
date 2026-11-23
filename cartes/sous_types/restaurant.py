from cartes.tasse import Tasse


class Restaurant(Tasse):
    def __init__(self):
        super().__init__("Restaurant", 3, [9, 10])

    def effet(self, joueur_t, joueur_p, liste_joueurs, banque, reserve):
        for monument in joueur_p.monuments:
            if monument.nom == "Centre commercial" and monument.est_construit:
                res = joueur_t.payer(joueur_p, 3)
                print(f"[Joueur {joueur_p.id+1}] (Restaurant) Le joueur {joueur_t._id+1} vous donne {res}")
            else:
                res = joueur_t.payer(joueur_p, 2)
                print(f"[Joueur {joueur_p.id+1}] (Restaurant) Le joueur {joueur_t._id+1} vous donne {res}")
                
            break
