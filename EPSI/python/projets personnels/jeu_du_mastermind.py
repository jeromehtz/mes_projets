'''
L'objectif du jeu est de deviner une combinaison secrète de chiffres dans un nombre limité d'essais. Voici les règles :

Combinaison secrète : Le programme génère une combinaison secrète de 4 chiffres (entre 0 et 9).
Entrée utilisateur : Le joueur a 10 tentatives pour deviner la combinaison.

__Indications__ :
Après chaque essai, le programme doit indiquer :
Combien de chiffres sont corrects et bien placés.
Combien de chiffres sont corrects mais mal placés.

__Fin du jeu__ :
Le joueur gagne s'il devine la combinaison exacte avant de dépasser les 10 tentatives.
Le programme affiche la solution si le joueur ne parvient pas à deviner la combinaison au bout de 10 essais.

__Exemple__ :

Combinaison secrète : 1234
Essai du joueur : 1325

__Résultat__ : 2 chiffres bien placés (1 et 3), 1 chiffre correct mais mal placé (2).
Le jeu doit se terminer lorsque le joueur trouve la combinaison ou lorsqu'il n'a plus d'essais.
'''

''' Fonction : vérifier si un chiffre est dans la liste et correctement placé'''

def in_list(chiffre, L, i) : #i correspond à l'index où se trouve le chiffre du joueur
    if chiffre in L :
        j = 0
        length_L = len(L)
        while j<length_L and L[j]!=chiffre :
            j+=1
        if j==i :
            return (True, True)
        return (True, False)
    else :
        return (False, False)

''' Fonction : convertir un nombre en liste de chiffres '''

def number_to_list(n) : 
    L = []
    i=0
    while n >= 1 :
        nbr = n//10
        reste = n%10
        if L==[] :
            L.append(reste)
        else :
            L.append(0)
            j=i
            while j>=1 :
                L[j-1], L[j] = L[j], L[j-1]
                j-=1
            L[j] = reste
        i+=1
        n=nbr
    return L

print(number_to_list(1234))