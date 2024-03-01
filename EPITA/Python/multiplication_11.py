"""
ne pas utiliser la multiplication par 11
ni ajouter le nombre 11 fois

principe :
prenons 99.
  -> on fait une addition avec retenues de chaque chiffre du nombre 2 à 2 voisins en
  gardant les extremites en ajoutant la retenue pour l'extremite gauche.
  
  Pour 99, cela se fait en 3 etapes :
    - on ecarte le 9 de droite
    - 9+9 = 18 => retenue = 1 car 18>9
    - donc on a pour le moment 89
    - et du coup, puisque l'on a une retenue de 1, 9+1 = 10
    => 99*11 = 1089
  autre exemple : 243*11 = 2673, je vous laisse verifier

je vais donc appliquer cet algorithme
"""

def multiplication_11(n) :
    n_str = str(n)
    i = len(n_str)
    res = ""
    res = res + n_str[i-1]
    retenue = 0
    resultat = 0
    while i!= 0 :
        i-=1
        if i==0 :
            resultat = int(n_str[i])+retenue
            if resultat >= 10 :
                res = str(resultat-10) + res
                retenue = 1
                res = str(retenue) + res
            else :
                res = str(resultat) + res
        else :
            resultat = int(n_str[i])+int(n_str[i-1])+retenue
            if resultat >=10 :
                res = str(resultat-10) + res
                retenue = 1
            else :
                res = str(resultat) + res
                retenue = 0
    return res
a = int(input("entrez la valeur de votre nombre : "))
print(a,"multiplie par 11, cela donne :",multiplication_11(a))