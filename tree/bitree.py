from collections import deque

class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


a = BiTreeNode("A")
b = BiTreeNode("B")
c = BiTreeNode("C")
d = BiTreeNode("D")
e = BiTreeNode("E")
f = BiTreeNode("F")
g = BiTreeNode("G")
h = BiTreeNode("H")

e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f
g.lchild = h

root = e

def pre_order(root):
    if root:
        print(root.data, end=',')
        pre_order(root.lchild)
        pre_order(root.rchild)


# 头，左，右
def pre_order_no_rec(root):
    queue1 = deque()
    queue1.append(root)
    while len(queue1) > 0:
        node = queue1.pop()
        print(node.data,end=',')
        if node.rchild:
            queue1.append(node.rchild)
        if node.lchild:
            queue1.append(node.lchild)
        

def in_order(root):
    if root:
        in_order(root.lchild)
        print(root.data,end=',')
        in_order(root.rchild)


def in_order_no_rec(root):
    queue = deque()
    while root != None or len(queue) > 0:
        if root != None:
            queue.append(root)
            root = root.lchild
        else:
            root = queue.pop()
            print(root.data,end=',')

            root = root.rchild
    


def post_order(root):
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data,end=',')

# 头，右，左，倒过来就是后序遍历
def post_order_no_rec(root):
    queue1 = deque()
    queue_res = deque()
    queue1.append(root)
    while len(queue1) > 0:
        node = queue1.pop()
        queue_res.append(node)
        if node.lchild:
            queue1.append(node.lchild)
        if node.rchild:
            queue1.append(node.rchild)
    
    while len(queue_res) > 0:
        node = queue_res.pop()
        print(node.data, end=',')

def post_order_no_rec_2(h):
    #h表示上次打印的节点
    #c，c表示当前节点，根据c和h的关系判断c需不需要打印
    queue = deque()
    # queue = []
    if h:
        queue.append(h)
        # c = None
        while len(queue) > 0:
            c = queue[-1]
            if c.lchild and h != c.lchild and h != c.rchild:
                queue.append(c)
            else:
                if c.rchild and h != c.rchild:
                    queue.append(c)
                else:
                    print(queue.pop().value,end=',')
                    h = c

# post_order_no_rec_2(root)


# 层次遍历  同样适用于多叉树
def level_order(root):
    queue = deque()
    queue.append(root)
    while len(queue) > 0:   #只要队不空
        node = queue.popleft()
        print(node.data)
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)




# pre_order(root)
# print('')
# pre_order_no_rec(root)

# in_order(root)
# print('')
# in_order_no_rec(root)

# post_order(root)
# print('')
# post_order_no_rec_2(root)
# level_order(root)