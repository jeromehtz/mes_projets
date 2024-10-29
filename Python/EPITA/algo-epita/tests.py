"""
print("on est quel jour ? \n")
d=int(input("jour : "))
print()
m=int(input("mois : "))
print()
y=int(input("année : "))
print()
"""
from complexite import *

def tomorrow(d,m,y) :
    if y>2021 or (m>12 or m<1) or (y%4==1 and m==2 and d>28) or (y%4==0 and m==2 and d>29) or (d>30 and (m==4 or m==6 or m==9 or m==11)) :
        print("non valide")
    elif d==30 and (m==4 or m==6 or m==9 or m==11) :
        print(1,"/",m+1,"/",y)
    elif d==31 and (m==1 or m==3 or m==5 or m==7 or m==8 or m==10) :
        print(1,"/",m+1,"/",y)
    elif d==31 and m==12 :
        print(1,"/",1,"/",y+1)
    else :
        print(d+1,"/",m,"/",y)

def list_to_9(n,t=0) :
    t+=1
    reverse = (n%10)*10+n//10
    a=n
    if a>99 :
        print(a,"is not a 2-digit positive integer")
        print(0)
    elif n==0 :
        print("no list to 9!")
        print(n)
    elif a<=9 :
        print(a)
        print(t)
    elif reverse>n :
        n,reverse = reverse,n
        a=reverse
        print(a)
        n = n-reverse
        return(list_to_9(n,t))
    elif reverse<n :
        print(a)
        n = n-reverse
        return(list_to_9(n,t))

def premier(n) :
    if n<=1 :
        raise Exception ("n must be > 1")
    else :
        nombre = n-1
        while (n%nombre)!=0:
            nombre -= 1
        return nombre==1

def premiers(n) :
    i=2
    liste = []
    while i<n :
        if premier(i) :
            liste.append(i)
        i+=1
    return liste

def factorielle(limite) :
    if limite <= 0 :
        raise Exception ("n must be positive")
    else :
        n=1
        compteur = 0
        while n<limite :
            n = n*(n+1)
            compteur+=1
        return compteur

def pgcd(a,b) :
    if a<0 or b<0 :
        raise Exception ("positif non nul")
    elif b == 0 :
        return a
    else :
        return pgcd(b,a%b)
#print(pgcd(17,4))

"""
def insert(L,x) :
    i = len(L)-1
    L.append(L[i])
    a = False
    while i>0 and a==False :
        if L[i]==x :
            raise Exception ("deja dans la liste")
        elif L[i-1]<x :
            L[i]=x
            a = True
        else :
            L[i]=L[i-1]
        i -= 1
    return L,a"""

def binaire(i) :
    liste = []
    j=i
    while i!=0 :
        if i==1 :
            liste.append(i)
            i-=1
        else :
            liste.append(i%2)
            i=i//2
    liste2 = []
    print(len(liste))
    if len(liste)<8 :
        count = 8-len(liste)
        while count < 8 :
            liste2.append(0)
            count+=1
    while len(liste)!=0 :
        a = liste.pop()
        liste2.append(a)
        i+=1
    return liste2

def complement_1(x) :
    if x<0 :
        x = -1*x
    liste = binaire(x)
    liste2 = []
    i = len(liste)
    while i != 0 :
        a=liste.pop()
        if a==1 :
            liste2.append(0)
        else :
            liste2.append(1)
        i-=1
    while len(liste2)!=0 :
        a = liste2.pop() 
        liste.append(a)
    return liste

def complement_2(x) :
    liste = complement_1(x)
    liste2 =[]
    retenue = 1
    while len(liste)!=0 :
        a = liste.pop()
        a = a + retenue
        if a == 2 :
            a=0
            retenue=1
        elif a==1 :
            retenue=0
        liste2.append(a)
    while len(liste2)!=0 :
        a = liste2.pop() 
        liste.append(a)
    return liste

def retourner(liste2) :
    liste=[]
    l = len(liste2)
    while l!=0 :
        a = liste2.pop() 
        liste.append(a)
        l-=1
    return liste

def from_int(x) :
    if x>0 :
        return binaire(x)
    elif x<0 :
        return complement_2(x)
    
def equals(a,b) :
    return b==2*a
def find2 (p,l1,l2) :
    if len(l1)!=len(l2) :
        raise Exception ("error : size")
    else :
        i=0
        while not p(l1[i],l2[i]) and i!=len(l1)-1 :
            i+=1
            
        if i==len(l1) :
            raise Exception ("error : it's not working")
        else :
            return l1[i],l2[i]

def search_indexes(liste,val) :
    if val not in liste :
        return (-1,-1)
    else :
        last_ind = 0
        premier = max(liste)+1
        for i in range(len(liste)) :
            if premier != max(liste)+1 and liste[i]==val :
                last_ind = i
            elif liste[i]==val :
                premier = i
        return premier,last_ind

def mult_10(n,i) :
    if i == 0 : 
        return 1
    else :
        return n*mult_10(n,i-1)

def int_to_list(n) :
    liste = []
    i = int(input("nombre de chiffres de votre nombre : "))
    i-=1
    while i!=0 :
        liste.append(n//(mult_10(10,i)))
        n=n%(mult_10(10,i))
        i-=1
    if n!=0 :
        return ("vous ne savez pas compter")
    return liste

def insert(x,L) :
    L.append(0)
    l = len(L)
    i, intermediaire = 0, 0
    while i<l :
        if x<L[i] :
            intermediaire = L[i]
            L[i] = x
            x = intermediaire
        elif i==l-1 and L[i]==0 :
            L[i] = x
        i+=1
    return L


def build_list(n) :
    import random
    liste = []
    for i in range(n) :
        nombre = random.randint(0,100)
        liste.append(nombre)
    return liste


 

def select_sort(L) :
    l = len(L)
    for i in range(l) :
        j = i+1
        indice = i
        memory = L[i]
        while j<l :
            if memory>L[j] :
                memory = L[j]
                indice = j
            j+=1
        if L[i] > L[indice] :
            (L[i], L[indice]) = (L[indice],L[i])
    return L

def select_sort_(L) :
    l = len(L)
    for i in range(l-1,-1,-1) :
        j,max = 0,L[0]
        ind_max=0
        while j<i :
            j+=1
            if L[j]>max :
                max = L[j]
                ind_max = j
        if L[ind_max]>L[i] :
            (L[ind_max],L[i]) = (L[i],L[ind_max])
    return L

def supprimer_enplace(L,k) :
    l = len(L)
    if k<0 or k>=l :
        raise Exception("supprimer_enplace : indice invalide")
    else :
        """
        le but est de deplacer la valeur a l'indice k a la fin
        et d'utiliser la fonction L.pop()
        en se mettant comme contrainte de ne pas utiliser 
        d'autres fonctions que celles-ci :
            -> L.pop() (et non L.remove(L[k]))
            -> L.append(argument)
            -> len(L)
        """
        for i in range(k+1, l) :
            L[k],L[i] = L[i], L[k]
        L.pop() #supprime le dernier element de la liste

def supprimer_pas_enplace(L,k) :
    l = len(L)
    if k<0 or k>=l :
        raise Exception("supprimer_pas_enplace : inice invalide")
    else :
        L1 = []
        for i in range(l) :
            if i!= k :
                L1.append(L[i])
        return L1

#print(l)
#liste = build_list(40000000)
#liste1 = liste

#complexite()
#complexite_()

"""
ecrire une fonction qui retourne le caractere le plus
frequent d'une chaine, ainsi que son nombre
d'occurences
"""
def init_list(n,val) :
    L = []
    for i in range(n) :
        L.append(val)
    return L
def histog_3(str) :
    max, l = 0, len(str)
    lettr = ''
    L_lettre = []
    for i in range(l) :
        nbr_char = 1
        lettre = str[i]
        if L_lettre == [] :
            L_lettre.append((nbr_char,lettre))
        else :
            j=0
            l1 = len(L_lettre)
            (occ,Lettre) = L_lettre[0]
            while j<l1 and Lettre!=lettre :
                (occ,Lettre) = L_lettre[j]
                j+=1
            if Lettre==lettre and j==0 :
                occ+=nbr_char
                L_lettre[j]=(occ,Lettre)
            elif Lettre==lettre :
                occ+=nbr_char
                L_lettre[j-1]=(occ,Lettre)
            else :
                #(occ,Lettre) = L_lettre[j-1]
                L_lettre.append((nbr_char,lettre))
            if occ>max :
                max=occ
                lettr = lettre
    return max,lettr

def dicho_list(x,L) :
    left, right = 0, len(L)
    l=right
    middle = right//2
    while left != right and L[middle]!=x :
        if x < L[middle] :
            right = middle
        else :
            left = middle + 1
        middle = (left + right)//2
    if middle<l and L[middle]==x :
        return middle
    else :
        return right

def init_list(n,val) :
    L = []
    for i in range(n) :
        L.append(val)
    return L

def erathostene(n) :
    L = init_list(n+1,True)
    L_primes = []
    i=2
    t=1
    while i<=n :
        t+=1
        j=i
        while j<n :
            j+=1
            if j%i==0 and L[j]==True :
                L[j]=False
        if L[i]==True :
            L_primes.append(i)
        i+=1
    print(t)
    return L_primes