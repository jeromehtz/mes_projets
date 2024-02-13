from algopy.bintree import BinTree
from algopy import bintree

B_tuto = BinTree(5, 
              BinTree(2, 
                    BinTree(-1, BinTree(4,None,None), None), 
                    BinTree(0,None,BinTree(11,None,None))),
              BinTree(12, 
                    BinTree(4, None, None), 
                    BinTree(1, BinTree(-2, None, BinTree(15, None, None)), None)))

perfect7 = BinTree(1, BinTree(2, BinTree(4, None, None), BinTree(5, None, None)), 
                  BinTree(3, BinTree(6, None, None), BinTree(7, None, None)))

perfect = BinTree('A', 
                  BinTree('B', 
                          BinTree('D', BinTree('H', None, None), BinTree('I', None, None)), 
                          BinTree('E', BinTree('J', None, None), BinTree('K', None, None))), 
                  BinTree('C', 
                          BinTree('F', BinTree('L', None, None), BinTree('M', None, None)), 
                          BinTree('G', BinTree('N', None, None), BinTree('O', None, None))))

def __check_huffman(B) : #B!=None
    if B.left != None :
        if B.right == None :
            return B.key !=None and len(B.key) == 1
        else :
            return False
    else :
        if B.right == None :
            return False
        else :
            return B.key == None \
                and __check_huffman(B.left) \
                    and __check_huffman(B.right)

def check_huffman(B) :
    if B==None :
        return True
    else :
        return __check_huffman(B)

def __sym(B1, B2) :
    if B1 == None or B2 == None :
        return B1 == B2
    else :
        if B1.key != B2.key :
            return False
        else :
            return __sym(B1.left, B2.right) \
                and __sym(B1.right, B2.left)


def symetric(B) :
    return B==None or __sym(B.left, B.right)


def __get_nodes_branch(B, x, n=1) :
    if B != None and B.key == x:
        return n
    else :
        if B == None :
            return 0
        elif B.key>x :
            return __get_nodes_branch(B.left, x, n+1)
        else :
            return __get_nodes_branch(B.right, x, n+1)

def get_nodes_branch(B, x) :
    if B==None :
        return 0
    else :
        return __get_nodes_branch(B, x)

def generation(B, x, y) :
    res_x = get_nodes_branch(B, x)
    return res_x != 0 and get_nodes_branch(B, y) == res_x


def print_tree(B, type = "") :
    if B == None :
        print(None)
        return None
    else :
        print(type, end = " [")
        if B.left and B.right :
            print("(", end = "")
            print(B.key, end = ") ")
            print(B.left.key, B.right.key, end = "] ")
            print_tree(B.left, "\\ fils gauche: /")
            print_tree(B.right, "\\ fils droit: /")
        elif B.left :
            print("(", end = "")
            print(B.key, end = ") ")
            print(B.left.key,"None", end = "] ")
            print_tree(B.left, "\\ fils gauche: /")
        elif B.right :
            print("(", end = "")
            print(B.key, end = ") ")
            print("None",B.right.key, end = "] ")
            print_tree(B.right, "\\ fils droit: /")
        else :
            print("(", end = "")
            print(B.key, end = ") ")
            print("None","None", end = "] ")
        return None
print_tree(B_tuto)



