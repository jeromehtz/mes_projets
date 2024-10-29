#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Undergraduate Epita - S2
Binary Trees: measures and DFS
'''

from algopy import bintree

#-------------------------------------------------------------------------------
#1.1

def size(B):
    '''
    B: bintree
    return the size of the bintree B
    '''
    if B == None:
        return 0
    else:
        return 1 + size(B.left) + size(B.right)

#-------------------------------------------------------------------------------
#1.2

def height(B):
    '''
    B: bintree
    return the height of the bintree B
    '''
    if B == None:
        return -1
    else:
        return 1 + max(height(B.left), height(B.right))


#-------------------------------------------------------------------------------
#1.3

'''
DFS: Depth-First Search
'''

def dfs(B):
    if B == None:
        # terminal case
        pass
    else:
        # preorder / prefix
        dfs(B.left)
        # inorder
        dfs(B.right)
        # postorder / suffix
        
        
def __myprint(x):
    '''
    print element x without endline
    '''
    print(x, sep='', end='')
  
  
def dfs_displayAA(B):
    '''
    B: bintree
    display the Algebraic Abstract Type representation of the bintree B
    '''
    if B == None:
        __myprint('_')
    else:
        __myprint('<' + str(B.key) + ',')     
        # + is the concatenation operator on sequences
        dfs_displayAA(B.left)
        __myprint(',')
        dfs_displayAA(B.right)
        __myprint('>')
        
#-------------------------------------------------------------------------------
#1.4

'''
Serialization
<r, G, D> is "(rGD)"
'''

def to_linear(B):
    '''
    B: bintree
    return the linear representation of the bintary tree B (str)
    '''
    if B == None:
        return "()"
    else:
        s = '('
        s = s + str(B.key)
        s = s + to_linear(B.left)
        s = s + to_linear(B.right)
        s = s + ')'
    return s 

def to_linear2(B):
    '''
    B: bintree
    return the linear representation of the binary tree B (str)
    '''
    if B == None:
        return "()"
    else:
        return '(' + str(B.key) + to_linear2(B.left) + to_linear2(B.right) + ')'
        
