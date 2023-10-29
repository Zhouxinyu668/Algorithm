class BiTreeNode:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None
     

class BST:
    def __init__(self,li=None):
        self.root = None
        if li:
            for val in li:
                self.insert_no_rec(val)

    def insert(self, node, val):
        if node == None:
            node = BiTreeNode(val)
        elif val < node.data:
            node.lchild = self.insert(node.lchild, val)
            node.lchild.parent = node
        elif val > node.data:
            node.rchild = self.insert(node.rchild, val)
            node.rchild.parent = node         
        return node
    
    def insert_no_rec(self,val):
        p = self.root
        if not p:
            self.root = BiTreeNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p
                    return
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    return
            else:
                return
    
    def query(self, node, val):
        if not node:
            return None
        elif node.data > val:
            return self.query(node.lchild,val)
        elif node.data < val:
            return self.query(node.rchild, val)
        else:
            return node
    
    def query_no_rec(self, val):
        p = self.root
        while p:
            if p.data < val:
                p = p.rchild
            elif p.data > val:
                p = p.lchild
            else:
                return p
        return None

    def __remove_node_1(self, node):
        #要删除的node
        #情况1：node是叶子节点
        if not node.parent:
            self.root = None
        if node == node.parent.lchild:  #node是它父亲的左孩子
            self.parent.lchild = None
        elif node == node.parent.rchild:    #node是右孩子
            self.parent.rchild = None
    
    def __remove_node_21(self, node):
        #情况2：node只有一个左孩子
        if not node.parent:
            self.root = node.lchild
            node.lchild.parent = None
        elif node == node.parent.lchild:  #node是它父亲的左孩子
            node.parent.lchild = node.lchild
            node.lchild.parent = node.parent
        else:
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent
    
    def __remove_node_22(self, node):
        #情况3：node只有一个右孩子
        if not node.parent:
            self.root = node.rchild
            node.rchild.parent = None
        elif node == node.parent.lchild:
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent
        elif node == node.parent.rchild:
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent

    def delete(self,val):
        if self.root:
            node = self.query_no_rec(val)
            if not node:
                return False
            if not node.lchild and not node.rchild:     #叶子节点
                self.__remove_node_1(node)
            elif not node.rchild:       #2.1只有一个左孩子
                self.__remove_node_21(node)
            elif not node.lchild:
                self.__remove_node_22(node)     #只有一个右孩子
            else:       #两个孩子都有
                min_mode = node.rchild
                while min_mode.lchild:
                    min_mode = min_mode.lchild
                node.data = min_mode.data
                #删除min_mode
                if min_mode.rchild:
                    self.__remove_node_22(min_mode)
                else:
                    self.__remove_node_1(min_mode)


    def pre_order(self, root):
        if root:
            print(root.data, end=',')
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)


    def in_order(self, root):
        if root:
            self.in_order(root.lchild)
            print(root.data,end=',')
            self.in_order(root.rchild)

    def post_order(self, root):
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data,end=',')


import random
li = list(range(0,5000,2))
random.shuffle(li)
tree = BST(li)
print(tree.query_no_rec(4).data)

# tree = BST([4,6,7,9,2,1,3,5,8])
# print(tree)
# tree.pre_order(tree.root)
# print("")
# # 输出的是排好序的
# tree.in_order(tree.root)
# print("")
# tree.post_order(tree.root)