#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 14:48:07 2022

@author: nathalie
"""
from algopy import bintree


def __build(B, L):
    if B != None:
        __build(B.left, L)
        L.append(B.key)
        __build(B.right, L)
    
def BST_to_list(B):
    L = []
    __build(B, L)
    return L

def __buildBST(L, start, end):
    """
    build a BST with values from L between 
    positions start (included) and end (not included)
    """
    if start == end:
        return None
    else:
        middle = (start + end) // 2
        B = bintree.BinTree(L[middle], None, None)
        B.left = __buildBST(L, start, middle)
        B.right = __buildBST(L, middle+1, end)
        return B
    
    
def list_to_BST(L):
    return (__buildBST(L, 0, len(L)))

infty = float('inf')

def __isBST(B, inf, sup):
    """
    test if B is a BST with its values in ]inf, sup]
    """
    if B == None:
        return True
    else:
        if B.key <= inf or B.key > sup: 
            return False
        else:
            return __isBST(B.left, inf, B.key) \
                and __isBST(B.right, B.key, sup)
            
            

def is_BST(B):
    return __isBST(B, -infty, infty) 


def minBST(B):
    if B.left == None:
        return B.key
    else:
        return minBST(B.left)
    
def maxBST(B):
    while B.right != None:
        B = B.right
    return B.key

def searchBST(B, x):
    if B == None or B.key == x:
        return B
    else:
        if x < B.key:
            return searchBST(B.left, x)
        else:
            return searchBST(B.right, x)
            
def search_iter(B, x):
    while B != None and B.key != x:
        if x < B.key:
            B = B.left
        else:
            B = B.right
    return B
            
            
            
def insert_leaf(B, x):
    if B == None:
        return bintree.BinTree(x, None, None)
    else:
        if x <= B.key:
            B.left = insert_leaf(B.left, x)
        else:
            B.right = insert_leaf(B.right, x)
        return B
        
        
def insert_iter(B, x):
    New = bintree.BinTree(x, None, None)
    if B == None:
        return New
    else:
        C = B
        while C != None:
            Dad = C
            if x <= C.key:
                C = C.left
            else:
                C = C.right
                
        if x <= Dad.key:
            Dad.left = New
        else:
            Dad.right = New
        return B
    
    

    
    
def del_BST(B, x):
    if B == None:
        return None
    else:
        if x == B.key:
            pass
            #FIXME
        else:
            if x < B.key:
                B.left = del_BST(B.left, x)
            else: # x > B.key
                B.right = del_BST(B.right, x)
            return B
    
    
    
    
    
    
        
   
