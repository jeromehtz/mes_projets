def binaire(n) :
    if n==1 :
        return 1
    elif n==0 :
        return 0
    else :
        return binaire(n//2),n%2
        
print(binaire(15))
def insert(x,L) :
    L.append(0)
    i, intermediaire = 0, 0
    while i<len(L) :
        if x<L[i] :
            intermediaire = L[i]
            L[i] = x
            x = intermediaire
        elif i==len(L)-1 and L[i]==0 :
            L[i] = x
        i+=1
    return L

def select_sort(L) :
    for i in range(len(L)-1) :
        j = i
        indice = 0
        memory = L[i]
        while j<len(L) :
            if memory>L[j] :
                memory = L[j]
                indice = j
            j+=1
        if L[i] != L[indice] :
            (L[i], L[indice]) = (L[indice],L[i])
    return L