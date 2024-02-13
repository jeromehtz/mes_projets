#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2022-12
Recursive -> Iterative
"""

from algopy import bintree
from algopy import stack

###############################################################################
#           One call

# tail-recursive function -> easy!

def left(B, l=-1):
    if B == None:
        print('\n length=', l)
    else:
        print(B.key, end=' ')
        left(B.left, l+1)

def left_iter(B):
    l = -1
    while B != None:
        print(B.key, end=' ')
        B = B.left
        l = l + 1
    print('\n length=', l)

# non tail recursive functions -> a stack is needed
    
def __leftBack(B):
    if B == None:
        return -1
    else:
        res = 1 + __leftBack(B.left)
        print(B.key, end=' ')
        return res

def leftBack(B):
    l = __leftBack(B)
    print("\n length =", l)


def leftBack_iter(B):
    # going down => push
    
    # going up => pop
    pass

###############################################################################
# two calls: dfs on a binary tree
# Exercise 6.2

def __dfs(B, pref, inf, suff):
    if B != None:
        pref.append(B.key)
        __dfs(B.left, pref, inf, suff)
        inf.append(B.key)
        __dfs(B.right, pref, inf, suff)
        suff.append(B.key)
        
def dfs(B):
    (pref, inf, suff) = ([], [], [])
    __dfs(B, pref, inf, suff)
    return(pref, inf, suff)
    
# iterative versions

    
# q.1, build only preorder list    
def dfs_pref_iter(B):
    pref = []
    if B != None:
        #FIXME
        pass
    return pref
