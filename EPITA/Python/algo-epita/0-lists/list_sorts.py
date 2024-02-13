# -*- coding: utf-8 -*-
"""
Lists: classical sorts
S1-S2
"""


#from algopy import listtools
from algopy import timing

    
"""
Selection sort
"""

def minimum(L, start, end):
    ''' search for the position of the mimimum in a list
    Args:
        L: a non empty list
        start, end: int / 0 <= start < end < len(L)
    Returns: 
        int: the position of the mimimum in L between the positions start included 
        and end exluded = [start, end[
    '''
    pos = start
    for i in range(start+1, end):
        if L[i] < L[pos]:
            pos = i
    return pos

# BONUS: another version, pretty :)
def minimum2(L, start, end):
    while (start < end):
        if L[start] < L[end]:
            end = end - 1
        else:
            start = start + 1
    return start
    
@timing.timing
def selectSort(L):
    '''
    selectSort(L) -> None -- sort L *IN PLACE*
    '''
    n = len(L)
    for i in range(n-1):
        pos = minimum(L, i, n)
        (L[i], L[pos]) = (L[pos], L[i]) # swap
        
'''
In one function, minimum inlined
'''

def selectSort2(L):
    n = len(L)
    for i in range(n-1):
        minpos = i
        for j in range(i + 1, n):
            if L[j] < L[minpos]:
                minpos = j
        (L[i], L[minpos]) = (L[minpos], L[i])

"""
Insertion sort
"""

def insert(x, L):
    '''
    insert(x, L) -> None -- insert x at its place in L sorted
    '''
    n = len(L)
# search position
    #FIXME    

# shifts
    #FIXME
    
# insertion
    L[i] = x

# BONUS
def insert2(x, L):
    '''
    search for place 
    and shifts at the same time
    '''
    #FIXME
    pass


@timing.timing    
def insertSort(L):
    '''
    insertSort(L) -> new sorted list
    '''
    
    R = []
    for x in L:
        insert2(x, R)
    return R
    

# BONUS: Insertion sort in place?

"""
Bubble sort (always in place)
"""

def bubble_sort(L):
    """
    sort in place the list L
    """
    #FIXME
    pass

