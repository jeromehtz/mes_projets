# -*- coding: utf-8 -*-
"""
S2 Matrices: maths and tests
2022-09
"""

import matrix
#import timing

#------------------------------------------------------------------------------
#1.3 Addition

# first version: the result matrix is built before
def add_matrices(A, B):
    '''
    A, B: non-empty matrices
    return the sum of matrices A and B
    '''
    (l, c) = (len(A), len(A[0]))
    if len(B) != l or len(B[0]) != c:
        raise Exception("add_matrices: Matrices do not have the same dimensions")
    M = matrix.init(l, c, 0)
    for i in range(l):
        for j in range(c):
            M[i][j] = A[i][j] + B[i][j]
    return M

# second version: the result matrix is built as we go along
def add_matrices2(A, B):
    '''
    A, B: non-empty matrices
    return the sum of matrices A and B
    '''
    (l, c) = (len(A), len(A[0]))
    if (l, c) != (len(B), len(B[0])):
        raise Exception("add_matrices2: Matrices do not have the same dimensions")
    M = []
    for i in range(l):
        L = []
        for j in range(c):
            L.append(A[i][j] + B[i][j])
        M.append(L)
    return M

#------------------------------------------------------------------------------
#1.4 Product
    
def mult_matrices(A, B):
    '''
    A, B: non-empty matrices
    return the product of matrices A and B
    '''
    m = len(A)
    n = len(A[0])
    if n != len(B):
        raise Exception("mult_matrices: incompatible dimensions")
    p = len(B[0])
    M = matrix.init(m, p, 0)
    for i in range(m):
        for j in range(p):
            for k in range(n):
                M[i][j] = M[i][j] + A[i][k] * B[k][j]
    return M


#------------------------------------------------------------------------------
# 2.1 Minimax

# 2 functions

def posmaxlist(L):
    ''' maximum position of list L, not empty '''
    p = 0
    for i in range(1, len(L)):
        if L[i] > L[p]:
            p = i
    return p

def posminimax(M):
    (min_i, min_j) = (0, posmaxlist(M[0]))
    for i in range(1, len(M)):
        max_j = posmaxlist(M[i])
        if M[i][max_j] < M[min_i][min_j]:
            (min_i, min_j) = (i, max_j)
    return (min_i, min_j)

# a single function
maxint = float('inf')

def posminimax2(M):
    mini = maxint
    (min_i, min_j) = (0,0)
    (l, c) = (len(M), len(M[0]))
    for i in range(l):
        max_j = 0
        for j in range(1, c):
            if M[i][j] > M[i][max_j]:
                max_j = j
        if M[i][max_j] < mini:
            mini = M[i][max_j]
            (min_i, min_j) = (i, max_j)
    return (min_i, min_j)


#--------------------------------------------------------------------
# 2.2 Search

def search_matrix(M, x):
    (lig, col) = (len(M), len(M[0]))
    found = False
    i = 0
    while i < lig and found == False :
        j = 0
        while j < col and found == False :
            if x == M[i][j] :
                found = True
            j += 1
        i += 1
    if found:
        return (i-1, j-1)
    else :
        return (-1, -1)

# found is the column index        
def search_matrix2(M, x):
    (lin, col) = (len(M), len(M[0]))
    i = 0
    found = -1  # the column if found
    while i < lin and found == -1:
        j = 0
        while j < col and M[i][j] != x:
            j += 1
        if j != col:
            found = j
        i += 1
    if found != -1:
        return (i-1, found) # or (i-1, j)
    else:
        return (-1, -1)
    
# without boolean
def search_matrix3(M, x):
    (lin, col) = (len(M), len(M[0]))
    i = 0
    j = col
    while i < lin and j == col:
        j = 0
        while j < col and M[i][j] != x:
            j += 1
        i += 1
    if j == col:
        return (-1, -1)
    else:
        return (i-1, j)


#------------------------------------------------------------------------------
#2.3 Symmetry

def symmetric(A):
    '''
    A: non-empty matrix
    return True if A is symmetric, False otherwise
    '''
    (l, c) = (len(A), len(A[0]))
    if l != c:
        raise Exception("symmetric: not a square matrix")
    i = 0
    j = -1
    while i < l and j == (i-1):
        j = 0
        while j < i and A[i][j] == A[j][i]:
            j += 1
        i += 1
    return i == l and j == (i-1)
    
