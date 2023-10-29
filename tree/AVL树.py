
from bst import *
class AVLNode(BiTreeNode):
    def __init__(self,data):
        BiTreeNode.__init__(self,data)
        self.bf = 0
    
class AVLTree(BST):
    def __init__(self, li=None):
        BST.__init__(self, li)
    
    def rotate_left(self, p, c)     #左旋
        s2 = c.lchild
        p.rchild = s2
        if s2:
            s2.parent = p
        c.lchild = p
        p.parent = c

        p.bf = 0
        c.bf = 0
    
    def rotate_right(self, p, c):
        s2 = c.rchild
        p.lchild = s2
        if s2:
            s2.parent = p

        c.rchild = p
        p.parent = c

        p.bf = 0
        c.bf = 0
    
    def rotate_right_left(self, p, c):
        g = c.lchild
        
        s3 = g.rchild
        c.lchild = s3
        if s3:
            s3.parent = c
        
        g.rchild = c
        c.parent = g

        s2 = g.lchild
        p.rchild = s2
        if s2:
            s2.parent = p

        g.lchild = p
        p.parent = g

        #更新bf
        if g.bf > 0:
            






    def insert_no_rec(self, val):
        pass