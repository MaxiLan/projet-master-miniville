from jeu import Jeu

print("Une nouvelle partie commence...")
nb_joueurs = 4  # int(input("Nombre de joueurs (entre 2 et 4): "))

jeu = Jeu(nb_joueurs)
# i = 1 # nombre limité de tours pour l'instant

while not jeu.est_fini:  # and i <= 8:
    jeu.jouer()
    # i += 1


### Tests
"""
jeu.joueurs[0].payer(jeu.joueurs[1], 1)

for j in jeu.joueurs:
    print(f"Id: {j.id}; Pièces --> {j.piece_1} un, {j.piece_5} cinq, {j.piece_10} dix")
"""
