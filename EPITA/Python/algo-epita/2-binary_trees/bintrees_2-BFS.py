#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Undergraduate Epita - S2
Binary Trees: BFS
'''

from algopy import bintree, queue

# How to use queue?
"""
q = queue.Queue() returns a new queue
q.enqueue(e) enqueues e in q (no return)
q.dequeue() deletes and returns the first element of q
q.isempty() tests whether q is empty.
"""

#-------------------------------------------------------------------------------
#2.1

'''
BFS: Breadth-First Search (Level order traversal) = parcours largeur
'''

def BFS(B):
    '''
    B: bintree
    prints the keys of the bintree B in hierarchical order
    '''
    if B != None:
        q = queue.Queue()
        q.enqueue(B)
        while not q.isempty():
            B = q.dequeue()
            print(B.key, end=' ')
            if B.left != None:
                q.enqueue(B.left)
            if B.right != None:
                q.enqueue(B.right)


"""
get_average
    return the list of the average key values per level of a binary tree
"""

# first version with end-levl marks (None)

def get_average(B):
    L = []       
    if B != None:
        (sum_keys, nb_nodes) = (0, 0)
        q = queue.Queue()
        q.enqueue(B)
        q.enqueue(None)
        while not q.isempty():
            B = q.dequeue()
            if B == None:
                L.append(sum_keys / nb_nodes)
                if not q.isempty():
                    q.enqueue(None)
                    (sum_keys, nb_nodes) = (0, 0)
            else:
                sum_keys += B.key
                nb_nodes += 1
                if B.left != None:
                    q.enqueue(B.left)
                if B.right != None:
                    q.enqueue(B.right)
    return L  

# second version with two queues
    
def get_average2(B)  :   
    L = []       
    if B != None:
        (sum_keys, nb_nodes) = (0, 0)
        q_out = queue.Queue()
        q_out.enqueue(B)
        q_in = queue.Queue()
        while not q_out.isempty():
            B = q_out.dequeue()
            sum_keys += B.key
            nb_nodes += 1
            if B.left != None:
                q_in.enqueue(B.left)
            if B.right != None:
                q_in.enqueue(B.right)
            # changing level?
            if q_out.isempty():
                L.append(sum_keys / nb_nodes)
                (sum_keys, nb_nodes) = (0, 0)
                (q_out, q_in) = (q_in, q_out)   # q_out = q_in
                                               #  q_in = queue.Queue()
    return L  

# another way
    
def get_average3(B)  :   
    L = []       
    if B != None:
        (sum_keys, nb_nodes) = (0, 0)
        q_out = queue.Queue()
        q_out.enqueue(B)
        q_in = queue.Queue()
        while not q_out.isempty():
            while not q_out.isempty():
                B = q_out.dequeue()
                sum_keys += B.key
                nb_nodes += 1
                if B.left != None:
                    q_in.enqueue(B.left)
                if B.right != None:
                    q_in.enqueue(B.right)
            # changing level
            L.append(sum_keys / nb_nodes)
            (sum_keys, nb_nodes) = (0, 0)
            (q_out, q_in) = (q_in, q_out)   
    return L  
