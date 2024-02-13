# -*- coding: utf-8 -*-
"""
Philosophers Stone
S2# - Matrix tutorial
"""

from algopy import matrix, timing

# uncomment the lines @timing.timing if you want to see the durations!
# matrices are assumed not empty in all the following functions

"""
the following lines should be in another file...

# Rappel : Pour charger une matrice
HP10 = matrix.load("files/HarryPotter10.txt")

# matrix in the subject
T = [[3, 1, 7, 4, 2],
     [2, 1, 3, 1, 1],
     [1, 2, 2, 1, 8],
     [2, 2, 1, 5, 3],
     [2, 1, 4, 4, 4],
     [5, 2, 7, 5, 1]]
"""


def posmax(L):
    '''
    position of the maximum value in list L, non empty
    '''
    pos = 0
    for i in range(1, len(L)):
        if L[i] > L[pos]:
            pos = i
    return pos


#----------------- Greedy Algorithm (algorithme glouton) ----------------------

#@timing.timing
def HarryPotter_greedy(T) :
    j = posmax(T[0])
    s = T[0][j]
    (lig, col) = (len(T), len(T[0]))
    for i in range(1, lig):
        pos = j
        if j > 0 and T[i][j-1] > T[i][pos]:
            pos = j - 1
        if j < col - 1 and T[i][j+1] > T[i][pos]:
            pos = j + 1
        j = pos
        s += T[i][j]
    return s    
        
# with the path
def HarryPotter_greedy_path(T):
    col = len(T[0])
    j = posmax(T[0])
    s = T[0][j]
    path = [j]
    for i in range(1, len(T)):
        jmax = j
        if j > 0 and T[i][j-1] > T[i][jmax]:
            jmax = j-1
        if j < col-1 and T[i][j+1] > T[i][jmax]:
            jmax = j+1
        j = jmax
        path.append(j)
        s += T[i][j]
    return (s, path)

#----------------- Dynamic Programming ------------------ ----


def build_max_matrix_down(T):
    l = len(T)
    c = len(T[0])
    M = matrix.init(l, c, 0)
    
    # copy the first line
    for j in range(c):
        M[0][j] = T[0][j]

    for i in range(1, l):
        M[i][0] = T[i][0] + max(M[i-1][0], M[i-1][1])
        for j in range(1, c-1):
            M[i][j] = T[i][j] + max(M[i-1][j-1], M[i-1][j], M[i-1][j+1])
        M[i][c-1] = T[i][c-1] + max(M[i-1][c-2], M[i-1][c-1])
    
    return M

# going up
def build_max_matrix(T):
    l = len(T)
    c = len(T[0])
    M = matrix.init(l, c, 0)
    
    # copy the last line
    for j in range(c):
        M[l-1][j] = T[l-1][j]

    for i in range(l-2, -1, -1):
        M[i][0] = T[i][0] + max(M[i-1][0], M[i-1][1])
        for j in range(1, c-1):
            M[i][j] = T[i][j] + max(M[i+1][j-1], M[i+1][j], M[i+1][j+1])
        M[i][c-1] = T[i][c-1] + max(M[i+1][c-2], M[i+1][c-1])
    
    return M

#@timing.timing
def HarryPotter(T):
    M = build_max_matrix_down(T)
    n = len(M)  # line nb
    return M[n-1][posMax(M[n-1])]


# with the path    
def HarryPotter_path(T):
    M = build_max_matrix(T)
    val = M[0][posmax(M[0])]
    (_, path) = HarryPotter_greedy_path(M)  # :)
    return (val, path)    

#----------------------------------------------------------------------
# Brut force... warning: can be long when l, c >= 15, 15

# without the path
# without the path
def brut(T, i, j, lines, cols):
    """
    return the value of the best path from (i, j) (going down) in T : lines x cols
    """
    if i == lines - 1:
        return T[i][j]
    else:
        valmax = brut(T, i+1, j, lines, cols)
        if j > 0:
            valmax = max(valmax, brut(T, i+1, j-1, lines, cols))
        if j < cols - 1:
            valmax = max(valmax,  brut(T, i+1, j+1, lines, cols))
        return (valmax + T[i][j])
    
#@timing.timing
def HarryPotterBrutForce(T):
    """
    T not empty, at least 2 x 2 cells
    """    
    (lig, col) = (len(T), len(T[0]))
    maxi = 0
    for j in range(col):
        maxi = max(maxi, brut(T, 0, j, lig, col))
    return maxi
    
# BONUS: build the path
# the list is returned (use +... really not optimized)
def brut_path(T, i, j, lines, cols):
    if i == lines - 1:
        return (T[i][j], [j])
    else:
        (m, L) = brut_path(T, i+1, j, lines, cols)
        if j > 0:
            (mleft, Lleft) = brut_path(T, i+1, j-1, lines, cols)
            if mleft > m:
                m = mleft
                L = Lleft
        if j < cols - 1:
            (mright, Lright) = brut_path(T, i+1, j+1, lines, cols)
            if mright > m:
                m = mright
                L = Lright
        return (m + T[i][j], [j] + L)


def HarryPotter_brutforce_path(T):
    
    maxi = 0
    (lines, cols) = (len(T), len(T[0]))
    for j in range(cols):
        (m, L) = brut_path(T, 0, j, lines, cols)
        if m > maxi:
            (maxi, Lmax) = (m, L)
    return (maxi, Lmax)

