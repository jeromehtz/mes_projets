#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S2#
binary trees: hierarchical representation and occurrences
"""

from algopy import bintree, queue, listTools

#-------------------------------------------------------------
# Hierarchical numbering

# 3.1 
"""
search_hier(B, x) search for the hierarchical number of the node containing x 
in the binary tree B
"""

def search_hier(B, x, i=1):
    """
    B: BinTree
    x: the vakue to search for
    i (optional): int = hierachical of B's root (if B not empty)
    return the hierarchical numer of x if in B, None otherwise)
    """
    if B == None:
        return None
    else:
        if B.key == x:
            return i
        else:
            res = search_hier(B.left, x, 2*i)
            if res != None:
                return res
            else:
                return search_hier(B.right, x, 2*i+1)
        
# 3.2
"""
from BinTree to hierarchical representation
"""

# version 1: the size of the tree is given (n)
#           -> the vector size has the maximum length :(

def __build_hier(B, T, i):
    '''
    B: bintree
    T: vector (list) to fill
    i: int = hierachical of B's root (if B not empty)
    fill the vector T with the hierarchical representation of B
    '''
    if B != None:
        T[i] = B.key
        __build_hier(B.left, T, 2*i)
        __build_hier(B.right, T, 2*i+1)
    
def build_hier(B, n):
    '''
    B: BinTree
    n: size of the bintree B
    build and return the hierarchical representation of B
    '''
    T = []          # build T 
    for _ in range (2**n):
        T.append(None)
    __build_hier(B, T, 1)
    return T

# version 2: the higher hierarchical number is computed by a first traversal 
#          = the size of the vector
    
def __max_hier(B, i=1):
    '''
    B: bintree
    i: int = hierachical of B's root (if B not empty)
    return the highest hierarchical number of nodes in B
    '''
    if B == None:
        return i // 2
    else:
        return max(__max_hier(B.left, 2*i),
                   __max_hier(B.right, 2*i+1))
    
def build_hier_bis(B):
    T = listTools.initlist(__max_hier(B)+1, None)
    __build_hier(B, T, 1)
    return T

# version 3 (Bonus): the list grows when needed (vector size is the highest "hierarchical number")

def __build_hier_3(B, T, i):
    if B != None:
        for _ in range(len(T), i+1): # extends the size of L to i+1
            T.append(None)
        T[i] = B.key
        __build_hier_3(B.left, T, 2*i)
        __build_hier_3(B.right, T, 2*i+1)

def build_hier_ter(B):
    T = []
    __build_hier_3(B, T, 1)
    return T
   

#-------------------------------------------------------------
# Occurrences:


# 3.3
"""
build the representation by list of occurrences
"""

def occurrences_list(B):
    '''
    B: BinTree
    returns the list of occurrences (str) of B's nodes
    note: 'ε' is char(949)
    result example: ['ε', '0', '1', '00', '10', '11', '000', '001', '111', '0010', '0011']
    '''
    L = []
    if B != None:
        q = queue.Queue()
        q.enqueue((B, ""))
        while not q.isempty():
            (B, occ) = q.dequeue()
            L.append(occ)
            if B.left != None:
                q.enqueue((B.left, occ+'0'))
            if B.right != None:
                q.enqueue((B.right, occ+'1'))
        L[0] = chr(949)
    return L          
                
#------------------------------------------------------------------------------
# 3.4
# prefix code

#Q3: the tree
B_codes = bintree.BinTree(' ', 
            bintree.BinTree('a', None, None),
            bintree.BinTree(' ', 
                    bintree.BinTree(' ', 
                            bintree.BinTree('u', None, None), 
                            bintree.BinTree('n', None, None)
                            ), 
                    bintree.BinTree(' ', 
                            bintree.BinTree(' ', 
                                    bintree.BinTree('f', None, None),
                                    bintree.BinTree('m', None, None)),
                            bintree.BinTree('H', None, None)
                            )
                    )
            )

#Q4:
                            
"""
Search for the code of a letter in a full binary tree containing letters in leaves
two versions:
    - the code is built going down
    - [bonus] the code is built going up
"""

           
# occ is built going down
def __searchOcc(B, c, occ=""):
    """
    B non empty FULL tree
    c: the character
    occ: the occurence of the root
    """
    if B.left == None:
        if B.key == c:
            return occ
        else:
            return None
    else:
        resLeft = __searchOcc(B.left, occ+'0')
        if resLeft != "":
            return resLeft
        else:
            return __searchOcc(B.right, occ+'1')
        
    
# Bonus: occ is built going up
def __searchOcc2(B, c):
    """
    B non empty FULL tree
    """
    if B.left == None:
        if B.key == c:
            return ""
        else:
            return None
    else:
        resLeft = __searchOcc2(B.left, c)
        if resLeft != None:
            return '0' + resLeft
        else:
            resRight = __searchOcc2(B.right, c)
            if resRight != None:
                return '1' + resRight
            else:
                return None
        
        
def search_code(B, c):
    '''
    B: FULL tree containg letters in leaves
    c: letter
    returns the code of the given letter c, None if not found
    '''

    if B == None:
        return None
    else:
        return __searchOcc2(B, c) #__searchOcc(B, c)
        
