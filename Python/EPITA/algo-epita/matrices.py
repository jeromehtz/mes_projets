def list_sorted(L, n) :
    max = L[0]
    i = 1
    while i<n and max < L[i] :
        max = L[i]
        i += 1
    return i==n

def matrix_sorted(M) :
    taille = len(M[0])
    if list_sorted(M[0], taille) :
        max = M[0][taille-1]
        i = 1
        length_M = len(M)
        while i<length_M and list_sorted(M[i], taille) and M[i][0]>max :
            max = M[i][taille-1]
            i += 1
        return i==length_M
    else :
        return False

def search_hier(B, x) :
    if B == None :
        return 0
    else :
        return __search_hier(B, x, 0)

def __search_hier(B, x, i) :
    if B == None :
        return i
    else :
        i = __search_hier(B.left, x, i+1)
        i = __search_hier(B.right, x, i+1)
        return i

B_tuto = BinTree(5,
              BinTree(2,
                    BinTree(-1, BinTree(4,None,None), None),
                    BinTree(0,None,BinTree(11,None,None))),
              BinTree(12,
                    BinTree(4, None, None),
                    BinTree(1, BinTree(-2, None, BinTree(15, None, None)), None)))
