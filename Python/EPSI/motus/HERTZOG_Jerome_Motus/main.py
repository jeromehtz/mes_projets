from motus import *

def lire_regles(file) :
    try:
        s = open(file, "rt", encoding = "utf-8")
        line = s.readline()
        while line != '':
            line = s.readline()
            print(line, end = "")
        s.close()
    except IOError as e:
        print("Une erreur de lecture a eu lieu")

def Game() :
    print("----- Bienvenue dans Motus -----")
    print("1. Règles du jeu")
    print("2. Démarrer une partie")
    print("3. Quitter")
    choix = int(input("Choix : "))
    mots = charger_mots("mots.txt")
    while choix != 3 :
        if choix == 2 :
            print("----- Nouvelle partie -----")
            mot_cache = choisir_mot(mots)
            length_mot_cache = len(mot_cache)
            print(f"Le mot caché contient {length_mot_cache-1} caractères et commence par {mot_cache[0]}")
            coups = length_mot_cache-1
            print("---")
            victoire = False
            while coups != 0 and not(victoire) :
                print(f"Il vous reste {coups} coups à jouer.")
                mot_saisie = get_mot(length_mot_cache-1)
                print(f"Votre mot contient :", end = "")
                victoire = test_mot(mot_cache, mot_saisie)
                coups -= 1
        print(mot_cache)
        print("Afficher les règles du jeu. 1")
        print("Voulez-vous démarrer une nouvelle partie ? 2")
        print("QUitter : 3")
        choix = int(input("Choix : "))
if __name__ == "__main__" :
    print("Jeu du Motus")
    Game()