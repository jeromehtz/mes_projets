# -*- coding: utf-8 -*-
"""
BinTree: examples
"""

from algopy import bintree
from algopy.bintree import BinTree

#Figure 1
B_tuto = BinTree(5, 
              BinTree(2, 
                    BinTree(-1, BinTree(4,None,None), None), 
                    BinTree(0,None,BinTree(11,None,None))),
              BinTree(12, 
                    BinTree(4, None, None), 
                    BinTree(1, BinTree(-2, None, BinTree(15, None, None)), None)))

#Figure 2                
B_quid = BinTree('V', 
                BinTree('D', 
                   BinTree('I', 
                      BinTree('Q', None,BinTree('U', None,None)),
                      None),
                   BinTree('S', 
                      BinTree('E', None,None),
                      BinTree('T', None,None))),
                BinTree('I', 
                   BinTree('E', 
                      None,
                      BinTree('R', None,None)),
                  BinTree('A', 
                      BinTree('T', None,None),
                      BinTree('S', None,None))))
                      
#Figure 6    
B6 = BinTree(0, 
              BinTree(1, 
                    BinTree(2, None, None), 
                    BinTree(3,BinTree(4,None,None),None)),
              BinTree(5, 
                    BinTree(6, None, BinTree(7,None,None)), 
                    BinTree(8, BinTree(9,None,None), None)))

# binary trees for hierarchical implementation



rightedge = BinTree(1, None, BinTree(3, None, BinTree(7, None, BinTree(15, None, None))))

perfect3 = bintree.BinTree(1,bintree.BinTree(2,None,None),bintree.BinTree(3,None,None))

perfect7 = BinTree(1, BinTree(2, BinTree(4, None, None), BinTree(5, None, None)), 
                  BinTree(3, BinTree(6, None, None), BinTree(7, None, None)))

complete10 = BinTree(1, 
                      BinTree(2, BinTree(4, BinTree(8, None, None), BinTree(9, None, None)), BinTree(5, BinTree(10, None, None), None)), 
                      BinTree(3, BinTree(6, None, None), BinTree(7, None, None)))

################################################################################
#binary trees for type tests

non_complete10 = BinTree(1, 
                      BinTree(2, BinTree(4, BinTree(8, None, None), BinTree(9, None, None)), BinTree(5, None, BinTree(11, None, None))), 
                      BinTree(3, BinTree(6, None, None), BinTree(7, None, None)))
                      
"""
degen1:
     'complete': False,
     'degenerate': True,
     'epl': 6,
     'height': 6,
     'nb_leaves': 1,
     'perfect': False,
     'size': 7
"""
degen1 = BinTree('A', 
                   None, 
                   BinTree('B', 
                           BinTree('C', 
                                   None, 
                                   BinTree('D', 
                                           None, 
                                           BinTree('E', 
                                                   None, 
                                                   BinTree('F', 
                                                           BinTree('G', None, None), 
                                                           None)
                                                           )
                                            )
                                    ), 
                            None)
                )

"""
non_degen1:
     'complete': False,
     'degenerate': False,
     'epl': 12,
     'height': 6,
     'nb_leaves': 2,
     'perfect': False,
     'size': 8
 """
non_degen1 = BinTree('A', 
                      None, 
                      BinTree('B', 
                              BinTree('C', 
                                      None, 
                                      BinTree('D', 
                                              None, 
                                              BinTree('E', 
                                                      None, 
                                                      BinTree('F', 
                                                              BinTree('G', None, None), 
                                                              BinTree('Z', None, None)
                                                              )
                                                      )
                                              )
                                      ), 
                                None)
                       )

"""
non_degen2:
     'complete': False,
     'degenerate': False,
     'epl': 10,
     'height': 7,
     'nb_leaves': 2,
     'perfect': False,
     'size': 9
"""
non_degen2 = BinTree('A', 
                     BinTree('Z', 
                             BinTree('B', 
                                     BinTree('C', 
                                             None, 
                                             BinTree('D', 
                                                     None, 
                                                     BinTree('E', 
                                                             None, 
                                                             BinTree('F', 
                                                                     BinTree('G', None, None), 
                                                                     None)
                                                            )
                                                    )
                                            ), 
                                    BinTree('X', None, None)
                                    ), 
                            None
                            ), 
                    None
                    )

"""
non_perfect1:
    degenerate: False
    height: 3
    size: 14
    perfect: False
    epl: 21
    complete: False
    nb_leaves: 7
"""
non_perfect1 = BinTree('A', 
                       BinTree('B', 
                               BinTree('D', 
                                       BinTree('H', None, None), 
                                       BinTree('I', None, None)), 
                               BinTree('E', 
                                       BinTree('J', None, None), 
                                       BinTree('K', None, None))), 
                       BinTree('C', 
                               BinTree('F', 
                                       BinTree('L', None, None), 
                                       None), 
                               BinTree('G', 
                                       BinTree('N', None, None), 
                                       BinTree('O', None, None))))

"""
non_perfect2:
    degenerate: False
    height: 3
    size: 8
    perfect: False
    epl: 9
    complete: False
    nb_leaves: 4
"""
non_perfect2 = BinTree('A', 
                       BinTree('B', 
                               BinTree('D', None, None), 
                               BinTree('E', None, None)), 
                       BinTree('C', 
                               BinTree('F', None, None), 
                               BinTree('G', None, BinTree('O', None, None))))

"""
complete:
    degenerate: False
    height: 3
    size: 12
    perfect: False
    epl: 17
    complete: True
    nb_leaves: 6
"""
complete = BinTree('A', 
                  BinTree('B', 
                          BinTree('D', BinTree('H', None, None), BinTree('I', None, None)), 
                          BinTree('E', BinTree('J', None, None), BinTree('K', None, None))), 
                  BinTree('C', 
                          BinTree('F', BinTree('L', None, None), None), 
                          BinTree('G', None, None)))

"""
perfect:
    perfect: True
    size: 15
    degenerate: False
    epl: 24
    complete: True
    height: 3
    nb_leaves: 8
"""
perfect = BinTree('A', 
                  BinTree('B', 
                          BinTree('D', BinTree('H', None, None), BinTree('I', None, None)), 
                          BinTree('E', BinTree('J', None, None), BinTree('K', None, None))), 
                  BinTree('C', 
                          BinTree('F', BinTree('L', None, None), BinTree('M', None, None)), 
                          BinTree('G', BinTree('N', None, None), BinTree('O', None, None))))
