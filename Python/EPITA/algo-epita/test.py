def init(l,c,val) :
    L=[]
    for i in range(l) :
        L1 = []
        for j in range(c) :
            L1.append(val)
        L.append(L1)
    return L

def str2intlist(s) :
    L,string = [],""
    i=0
    string_1 = ""
    while i<len(s) and string_1 != "\\n" :
        if s[i] != " " and s[i]!='\\' and s[i]!='n' :
            string = string + s[i]
        elif s[i]=='\\' :
            string_1 += s[i]
        elif string_1 == "\\" :
            if s[i]=='n' :
                string_1 += s[i]
            else :
                raise Exception ("after \\ it has to be 'n'")   
        else:
            L.append(int(string))
            string = ""
        i+=1
    if s[i-1]!='n' :
        L.append(int(s[i-1]))
    return L

def load(filename) :
    f = open(filename)
    L = f.readlines()
    M = []
    for x in L :
        li = str2intlist(x)
        M.append(li)
    f.close()
    return M

def add_matrices(A,B) :
    if len(A)!=len(B) :
        raise Exception ("Les matrices ne sont pas de meme taille.")
    else :
        for i in range(len(A)) :
            if len(A[i])!=len(B[i]) :
                raise Exception ("Les matrices ne sont pas de meme taille.")
            else :
                for j in range(len(A[i])) :
                    A[i][j] += B[i][j]
        return A

def mult_matrices(A,B) :
    if len(A[0])!=len(B) :
        raise Exception("error")
    M = []
    p,n = len(B[0]),len(B)
    for i in range(len(A)) :
        line = []
        for j in range(p) :
            s = 0
            for k in range(n) :
                s+=A[i][k]*B[k][j]
            line.append(s)
        M.append(line)
    return M

def gaplist(L) :
    maxi, mini = L[0], L[0]
    for i in range(1,len(L)) :
        maxi,mini = max(maxi,L[i]),min(mini,L[i]) 
    return maxi-mini

def maxgap(M) :
    maxgap = gaplist(M[0])
    for i in range(1,len(M)) :
        maxgap = max(maxgap,gaplist(M[i]))
    return maxgap

def symetric(M) :
    test = True
    i=1
    while i<len(M) and test :
        j=0
        while j<i and test :
            test = M[i][j]==M[j][i]
            j+=1
        i+=1
    return test

def list_sorted(L) :
    n = len(L)
    test = True
    i=1
    while i<n and test==True :
        if not(L[i-1]<L[i]) :
            test=False
        i+=1
    return test

def matrix_sorted(M) :
    n,m=len(M),len(M[0])
    test,i = True,1
    list_sorted(M[0])
    value = M[0][m-1]
    while i<n and test==True :
        m1 = len(M[i])
        if M[i][0]<value or not(list_sorted(M[i])):
            test = False
        else :
            value = M[i][m1-1]
        i+=1
    return test

"""
def siamoise(n) :
    if n%2==0 or n<=2 :
        raise Exception("Siamoise : n is not valid.")
    M=init(n,n,0)
    x, y = n//2, n-1
    i = 2
    j=0
    M[i][x] = 1
    while i<(n*n)+1 :
        x1 = (x+1)%n
        y1 = (j+1)%n
        if M[y1][x1]==0 :
            M[y1][x1]=i
            x, y = x1, y1
        else :
            y-=1
            if y==-1 :
                y=n-1
            M[y][x]=i
        i+=1
    return M
print(siamoise(9))
"""


"""
Harry potter :
methode 1 : algorithe glouton 
    -> chercher le max local a chaque iteration
    -> construire le chemin d'une ligne a une autre
"""










"""
resultat = int

# 1)
resultat = c*nbr
print (resultat)

def f(c):
    resultat2 = c*nbr
    return resultat2
print(f(c))
"""
# 2)
"""
resultat = int#(input("saisir un nombre : "))
"""



def palindrome_1(str) :
    i,j = 0, len(str)-1
    bool_i, bool_j = False, False
    b = True
    while j>i and b :
        if str[i]==" " and bool_i==False :
            i+=1
            bool_i = True
        if str[j]==" " and bool_j==False :
            j-=1
            bool_j = True
        if str[i]==str[j] and str[i]!=" " and  str[j]!=" ":
            i,j = i+1, j-1
            bool_i, bool_j = False, False
        else :
            b=False
    return b


def complement_2(binaire) :
    #binaire est de type string
    string = ""
    i,bool = len(binaire) - 1, False
    while i>=0 :
        if binaire[i]=='1' and bool == False :
            string = '1' + string
            bool = True
        elif bool==True :
            if binaire[i]=='1' :
                string = '0' + string
            if binaire[i]=='0' :
                string = '1' + string
        else :
            string = binaire[i] + string
        i-=1
    return string

def binaire_non_signe(n) :
    if n==1 :
        return '1'
    elif n==0 :
        return '0'
    else :
        return binaire_non_signe(n//2) + str(n%2) + ""

def binaire_signe(n,i) :
    if n>=0 :
        print("ici")
        string = binaire_non_signe(n)
        taille = len(string)
        i-=taille
        while i>0 :
            string = '0' + string
            i-=1
        return string
    else :
        print("la")
        string = binaire_non_signe(-1*n)
        taille = len(string)
        i-=taille
        while i>0 :
            string = '0' + string
            i-=1
        return complement_2(string)
print(binaire_signe(-42,8))