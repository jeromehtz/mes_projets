"""
petite explication -> README.md
"""
# Imports
from random import sample, randint

# Fonction tirage_jeton pour tirer un jeton aléatoirement
def tirage_jeton(liste):
    indice = randint(0, len(liste)-1)
    return liste[indice]

# Fonction retirer_jeton pour retirer un jeton de la liste
def retirer_jeton(liste, jeton):
    liste.remove(jeton)

# Fonction afficher_grille_bingo pour afficher la grille de bingo
def afficher_grille_bingo(grille):
    for ligne in grille:
        print("[", end=" ")
        for element in ligne:
            print("{:4}".format(element), end=" ")
        print("]")

# Fonction generer_grille_bingo pour générer la grille de bingo
# Création d'une liste de n valeurs val
def liste_val(val, n) :
    liste = []
    for i in range(n) :
        liste.append(val)
    return liste
def generer_grille_bingo(liste_jetons):
    # Création d'une grille vide de 3 lignes par 9 colonnes
    # grille_bingo = [[0] * 9 for _ in range(3)]
    grille_bingo = []
    for _ in range(3) :
        liste_0 = liste_val(0, 9)
        grille_bingo.append(liste_0)
    
    # Tirage aléatoire de 15 jetons à partir de la liste de jetons
    num_grille = sample(liste_jetons, 15)
    
    # Répartir les jetons dans la grille
    for i in range(3):
        indices_vide = [j for j in range(9)]  # Liste des indices vides dans la ligne
        for _ in range(5):
            jeton = tirage_jeton(num_grille)
            ind = indices_vide.pop(randint(0, len(indices_vide) - 1))
            grille_bingo[i][ind] = jeton
            retirer_jeton(num_grille, jeton)  # Retirer le jeton utilisé
    
    return grille_bingo

# Fonction Game pour faire tourner le jeu
def Game():
    jetons = [i for i in range(1, 91)]
    victoire = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    ligne_de_0 = [0, 0, 0, 0]
    grille_bingo = generer_grille_bingo(jetons)
    afficher_grille_bingo(grille_bingo)
    length_grille_bingo = len(grille_bingo)
    while jetons:  # Tant qu'il reste des jetons dans la liste
        jeton_tire = tirage_jeton(jetons)
        retirer_jeton(jetons, jeton_tire)
        print(f"Numéro tiré : {jeton_tire}")
        afficher_grille_bingo(grille_bingo)

        i, j = 0, 0
        booleen = False # on n'a pas trouvé l'élément
        while i<length_grille_bingo and not(booleen) :
            liste = grille_bingo[i]
            if liste != ligne_de_0 :
                liste = grille_bingo[i]
                length_liste=len(liste)
                while j<length_liste and liste[j] != jeton_tire :
                    j+=1
                if j<length_liste :
                    booleen = True
                    liste.remove(jeton_tire)
                grille_bingo[i]=liste
                if liste == ligne_de_0 :
                    print("Félicitations ! Vous avez rempli une ligne !")
            i+=1
            

        if booleen:
            print("Félicitations ! Vous avez trouvé une valeur :", jeton_tire)
        
        #input()
    if grille_bingo == victoire :
        print("Bingo !")

    if not jetons:
        print("Vous avez tiré 90 jetons, vous avez perdu.")

Game()
