#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 10:26:56 2022

@author: nathalie
"""
from algopy import bintree, queue

def __get_singles(B, sibling):
    if B.left == None:
        if B.right == None:
            if sibling:
                return (0, 0)
            else:
                return (1, 0)
        else:
            (leaves, singles) = __get_singles(B.right, False)
            return (leaves, singles+1)
    else:
        if B.right == None:
            (leaves, singles) = __get_singles(B.left, False)
            return (leaves, singles+1)
        else:
            (l_left, s_left) = __get_singles(B.left, True)
            (l_right, s_right) = __get_singles(B.right, True)
            return (l_left + l_right, s_left + s_right)
        
        
def get_singles(B):
    if B == None:
        return (0, 0)
    else:
        return __get_singles(B, False)  
    
#############################" types
        
# degenerate
        
def __fili(B):  # B != None
    if B.left == None:
        if B.right == None:
            return True           
        else:
            return __fili(B.right)
    else:
        if B.right == None:
            return __fili(B.left)
        else:
            return False
        
def degenerate(B):
    if B == None:
        return True
    else:
        return __fili(B)

def __fili2(B):  # B != None
    if B.left == None:
        return B.right == None or __fili2(B.right)
    else:
        return B.right == None and __fili2(B.left)
        
def degenerate2(B):
    return B == None or __fili2(B)

# structure
def nodes_types(B): # B not empty
    if B.left == None:
        if B.right == None:
            # leaf
            pass
        else:
            # single right
            pass
    else:
        if B.right == None:
            # single left
            pass
        else:
            #double
            pass

def __perfect(B, h, depth=0): # B not empty
    if B.left == None:
        if B.right == None:
            return h == depth
        else:
            return False
    else:
        if B.right == None:
            return False
        else:
            return __perfect(B.left, h, depth+1) and __perfect(B.right, h, depth+1)
            
def __leftlength(B):
    """
    returns the length of the left branch
    """
    h = -1
    T = B
    while T != None:
        h += 1
        T = T.left
    return h

def is_prefect(B):  # complet 
    if B == None:
        return True
    else:
        return __perfect(B, __leftlength(B))
    
def perfect_up(B):    
    if B.left == None:
        if B.right == None:
            return (True, 0)
        else:
            return (False, -1)
    else:
        if B.right == None:
            return (False, -1)
        else:
            (ok_left, h_left) = perfect_up(B.left)
            if not ok_left: 
                return (False, -1)
            else:
                (ok_right, h_right) = perfect_up(B.right)
                return (ok_right and h_left == h_right, h_left+1)
    

def perfect_BFS(B):
    ok = True       
    if B != None:
        q = queue.Queue()
        q.enqueue(B)
        q.enqueue(None)
        cur = 0
        expected = 1
        while not q.isempty() and ok:
            B = q.dequeue()
            if B == None:
                ok = cur == expected
                if not q.isempty():
                    q.enqueue(None)
                    expected = 2 * cur
                    cur = 0
            else:
                cur += 1
                if B.left != None:
                    q.enqueue(B.left)
                if B.right != None:
                    q.enqueue(B.right)
    return ok

# second version with two queues
    
def is_prefect_bfs(B)  :   
    perfect = True
    if B != None:
        
        q_out = queue.Queue()
        q_out.enqueue(B)
        q_in = queue.Queue()
        cur = 0
        expected = 1
        while not q_out.isempty() and perfect:
            B = q_out.dequeue()
            cur += 1
            if B.left != None:
                q_in.enqueue(B.left)
            if B.right != None:
                q_in.enqueue(B.right)
            # changing level?
            if q_out.isempty():
                perfect = cur == expected
                expected = cur
                cur = 0
                (q_out, q_in) = (q_in, q_out)   # q_out = q_in
                                               #  q_in = queue.Queue()
    return perfect  
    
    
    
    
    
    
    
    
