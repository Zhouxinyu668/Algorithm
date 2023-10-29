from bitree import *
from collections import deque




def pre_order_series(root,res):
    if root:
        res.append(root.data)
        pre_order_series(root.lchild,res)
        pre_order_series(root.rchild,res)
    else:
        res.append(None)
    return res

def bulidByPreOrder(pre_list):
    value = pre_list.popleft()
    if value == None:
        return None
    root = BiTreeNode(value)
    root.lchild = bulidByPreOrder(pre_list)
    root.rchild = bulidByPreOrder(pre_list)
    return root

def level_order_series(root,res):
    queue = deque()

    if root == None:
        res.append(None)
    else:
        res.append(root.data)
        queue.append(root)
        while len(queue) > 0:
            root = queue.popleft()
            if root.lchild:
                res.append(root.lchild.data)
                queue.append(root.lchild)
            else:
                res.append(None)
            if root.rchild:
                res.append(root.rchild.data)
                queue.append(root.rchild)
            else:
                res.append(None)
    return res

def bulidByLevelOrder(res):
    val = res.popleft()
    if val == None:
        return None
    root = BiTreeNode(val)
    queue = deque()
    queue.append(root)

    while len(queue) > 0:
        node = queue.popleft()
        node.lchild = generate_Node(res.popleft())
        node.rchild = generate_Node(res.popleft())
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)
    return root


def generate_Node(val):
    if val:
        return BiTreeNode(val)
    else:
        return None

res = deque()

# res = level_order_series(root,res)
# print(res)

# root = bulidByLevelOrder(res)
# level_order(root)


result = deque()
res = pre_order_series(root,result)
print(res)

head = bulidByPreOrder(res)
pre_order(head)
print(head)