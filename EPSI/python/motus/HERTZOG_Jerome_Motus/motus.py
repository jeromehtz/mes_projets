from rich import print
from random import randint
# test
# test
# test
# test
# print("[red]H[/red]")

def get_mot(len_mot) :
    print(len_mot)
    mot = input("Entrez votre mot de "+str(len_mot)+" caractères :")
    while (len(mot)) != len_mot :
        mot = input("Entrez votre mot de "+str(len_mot)+" caractères :")
    return mot

def get_nombre_aleatoire(mini, maxi) :
    return randint(mini, maxi)

def charger_mots(file) :
    liste_mots = []
    try :
        s = open(file, "rt")
        line = s.readline()
        while line != '' :
            mot = ""
            for ch in line :
                mot = mot + ch
            if len(mot) >= 6 and len(mot) <= 8 :
                liste_mots.append(mot)
            line = s.readline()
        s.close()
    except IOError as e :
        print("Une erreur de lecture a eu lieu")
    return liste_mots

def choisir_mot(mots) :
    return mots[get_nombre_aleatoire(0, len(mots)-1)]

def test_mot(mot_cache, mot_saisie) :
    length_mot_saisie = len(mot_saisie)
    length_mot_cache = len(mot_cache)
    booleen = True
    for i in range(length_mot_saisie) :
        if mot_cache[i] == mot_saisie[i] :
            print(f"[red]{mot_saisie[i]}[/red]", end = "")
            booleen = (booleen and True)
        else :
            j = 0
            booleen2 = False
            while j<length_mot_cache and not(booleen2) :
                if i != j and mot_saisie[i]==mot_cache[j] :
                    print(f"[yellow]{mot_saisie[i]}[/yellow]", end = "")
                    booleen2 = True
                j+=1
            if not(booleen2) :
                print(mot_saisie[i], end = "")
            booleen = False
    print()
    return booleen

