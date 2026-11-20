from jeu import Jeu

print("Une nouvelle partie commence...")
nb_joueurs = 4  # int(input("Nombre de joueurs (entre 2 et 4): "))

jeu = Jeu(nb_joueurs)

while not jeu.est_fini:
    jeu.jouer()

### Tests
jeu.joueurs[0].payer(jeu.joueurs[1], 1)

for j in jeu.joueurs:
    print(f"Id: {j.id}; Pièces --> {j.piece_1} un, {j.piece_5} cinq, {j.piece_10} dix")
