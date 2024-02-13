def calculatrice() :
    res = 0
    reponse = input("Voulez-vous calculer votre moyenne ? oui/non ")
    if reponse=="oui" :
        t=int(input("Nombre de notes : "))
        i=t
        while t!=0 :
            t-=1
            note = int(input("La note : "))
            res+=note
        return res/i
    else :
        raise Exception("Pourquoi avez-vous lancé la calculatrice ?")
print(calculatrice())