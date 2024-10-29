#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Undergraduate Epita - S2
Binary Trees: build trees
'''

from algopy import bintree

#-------------------------------------------------------------------------------

"""
Structure algo de création d'arbre

def build(....):
    if ???:
        return None
    else:
        B = bintree.BinTree(key, None, None)   
        B.left = build(???)
        B.right = build(???)
        return B
        
ou
        return bintree.BinTree(key, build(...), build(....))        
"""

#-------------------------------------------------------------------------------
# 5.1: hierarchical implementation -> BinTree

def __build_bintree(T, n, i=1):
    '''
    H: vector representing a bintree in hierarchical representation
    n: T's size
    i: current position in the vector H
    builds and returns the BinTree version of H
    '''
    if i >=n or T[i] == None:
        return None
    else:
        L = __build_bintree(T, n, 2*i)
        R = __build_bintree(T, n, 2*i+1)
        B = bintree.BinTree(T[i], L, R)
        return B
    
def hier_to_BinTree(T):
    return __build_bintree(T, len(T))

#------------------------------------------------------------------------------
# 5.2: Copy With Size
    
class BinTreeSize:
    def __init__(self, key, left, right, size):
        self.key = key
        self.left = left
        self.right = right
        self.size = size


def copywithsize(B):
    #FIXME
    pass
    
#-------------------------------------------------------------------------------
# 5.3: linear reporesentation -> BinTree [Bonus]

def __from_linear(s, i):
    '''
    s: string representing a binary tree
    i: current position in the string s
    returns (tree, pos):
    - tree: BinTree version of s
    - i: new position in the string s
    '''
    #FIXME
    pass
        
def from_linear(s):
    '''
    s: string linear representation a binary tree (assumed correct)
    builds and returns the BinTree version of s
    '''
    (T, _) = __from_linear(s, 0)
    return T
