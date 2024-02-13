"""
ne pas utiliser la multiplication par 11
ni ajouter le nombre 11 fois

principe :
prenons 99.
  -> on fait une addition avec retenues de chaque chiffre du nombre 2 à >2 voisins en
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
def retourner(liste2) :
    liste=[]
    while len(liste2)!=0 :
        a = liste2.pop() 
        liste.append(a)
    return liste

def multiplication_11(n_liste) :
    liste = []
    i = len(n_liste)
    liste.append(n_liste[i-1])
    retenue = 0
    resultat = 0
    while i!= 0 :
        i-=1
        if i==0 :
            resultat = n_liste[i]+retenue
            if resultat >= 10 :
                liste.append(resultat-10)
                retenue = 1
                liste.append(retenue)
            else :
                liste.append(resultat)
        else :
            resultat = n_liste[i]+n_liste[i-1]+retenue
            if resultat >=10 :
                liste.append(resultat-10)
                retenue = 1
            else :
                liste.append(resultat)
                retenue = 0
    return retourner(liste)

def mult_10(n,i) :
    if i == 0 : 
        return 1
    else :
        return n*mult_10(n,i-1)


def mult_11(n) :
    n_liste = []
    j=0
    i = int(input("nombre de chiffres de votre nombre : "))
    i=i-1
    while i!=-1 :
        n_liste.append(n//(mult_10(10,i)))
        n=n%(mult_10(10,i))
        i-=1
        j+=1
    if n_liste[0]>9 or n_liste[0]<1 :
        raise Exception("Vous ne savez pas compter.")
    else :
        liste = multiplication_11(n_liste)
        i = 0
        j=len(liste)-1
        resultat = 0
        while j>=0 :
            resultat = liste[j]*mult_10(10,i) + resultat
            i+=1
            j-=1
        return resultat
a = int(input("entrez la valeur de votre nombre : "))
print(a,"multiplie par 11, cela donne :",mult_11(a))