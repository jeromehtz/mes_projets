# -*- coding: utf-8 -*-
"""
to help testing functions on random lists
"""
from random import randint

def init(n, val):
    '''
    build a fresh new list of length n full of val
    '''
    L = []
    for _ in range(n):
        L.append(val)
    return L

def buildRandomList(n, maxval):
    '''
    build a list with n random values in [0, maxval]
    '''
    L = []
    for i in range(n):
        L.append(randint(0, maxval))
    return L
    
def buildRandomSortedList(n, step):
    '''
    build a sorted list with n natural integers
    step is the maximum difference between values
    '''
    L = [0]
    for i in range(1, n):
        L.append(L[i-1] + randint(0, step))
    return L

def reverse(L):
    """
    reverse the list L in place -> None
    """
    n = len(L)
    for i in range(n//2):
        (L[i], L[n-i-1]) = (L[n-i-1], L[i])
    
def is_sorted(L):
    """
    Return whether the list L is sorted in increasing order
    """
    i = 0
    n = len(L)
    while i < n-1 and L[i] <= L[i+1]:
        i += 1
    return i == n-1
