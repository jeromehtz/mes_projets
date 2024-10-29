"""
L'ordi choisi a chaque tour un chiffre entre 0 et 9.
Si le joueur trouve le chiffre de l’ordi il construit une maison.
Au bout de 3 maisons, un village est alors construit.
Des qu’un village est construit, le compteur des maisons retourne a 0.
Si 3 villages minimum sont construits, le joueur a gagne.

Le joueur a 20 essais maximum pour construire le plus de villages possibles.
Il a a chaque tour 3 essais pour trouver le nombre de l’ordi, sachant que bien evidemment
il est genere aleatoirement et peut ainsi varier.
"""






def CheckNumber(input,number) :
    return input==number

def FindNumber(number,tries) :
    nombre = int(input())
    while not CheckNumber(nombre,number) and tries != 1 :
        tries-=1
        nombre = int(input())
    if nombre==number :
        return True
    return False

def Game() :
    import random
    print("Vous avez demmare une nouvelle partie.")
    print("--------------------------------------")
    print("L'ordi choisi a chaque tour un chiffre entre 0 et 9. \n Si le joueur trouve le chiffre de l’ordi il construit une maison. Au bout de 3 maisons, un village est alors construit. \n Des qu’un village est construit, le compteur des maisons retourne a 0. Si 3 villages minimum sont construits, le joueur a gagne. \n \n Le joueur a 20 essais maximum pour construire le plus de villages possibles. \n Il a a chaque tour 3 essais pour trouver le nombre de l’ordi, sachant que bien evidemment il est genere aleatoirement et peut ainsi varier.")
    essais = 20
    maison = 0
    village = 0
    tours = 0
    while essais != 0 :
        tours+=1
        new_value = random.randint(0,5)
        print("Quel est mon chiffre?")
        res = FindNumber(new_value,3)
        if res and maison==3 :
            village+=1
            maison=0
            print("Vous venez de construire un village.")
        elif res :
            maison+=1
            print("Vous venez de construire une maison.")
        else :
            print("Mon chiffre etait :",new_value)
        essais-=1
        print(tours,"****")
    if village>=3 :
        print("Vous avez gagne.")
        print("Vous avez construit",village,"villages.")
    else :
        print("Vous avez perdu.")
        print("Vous avez construit",village,"village(s).")

Game()
print("Vous avez fini votre partie.",end = "")
sortie = input()
