from collections import deque
from bitree import *


# 输出最大宽度
def TreeMaxWidth(root):
    if root == None:
        return 0
    queue = deque()
    queue.append(root)

    #key:node,value:在哪一层
    dict1 = {}
    dict1[root] = 1

    cur_level = 1       #当前正在统计哪一层的宽度
    cur_level_width = 0     #当前层的宽度,出来时再算
    max_width = 0

    while len(queue) > 0:
        node = queue.popleft()
        cur_node_level = dict1.get(node)
        if node.lchild:
            dict1[node.lchild] = cur_node_level + 1
            queue.append(node.lchild)
        if node.rchild:
            dict1[node.rchild] = cur_node_level + 1
            queue.append(node.rchild)
        if cur_node_level == cur_level:   #当前节点所在的层和当前层，如果不一致，就该结算当前层的节点数量，如果一致，就+1
            cur_level_width += 1
        else:
            max_width = max(max_width, cur_level_width)
            cur_level += 1
            cur_level_width = 1
    max_width = max(max_width, cur_level_width)
    return max_width


# width = TreeMaxWidth(root)
# print(width)

def TreeMaxWidthNoMap(root):
    queue = deque()
    queue.append(root)

    cur_end = root      #当前层最右节点是谁
    next_end = None     #如果有下一层的话，下一层最右节点是谁
    max_width = 0
    cur_level_node = 0      # 当前层的节点数

    while len(queue) > 0:
        node = deque.popleft()

        if node.lchild:
            queue.append(node.lchild)
            next_end = node.lchild
        if node.rchild:
            queue.append(node.rchild)
            next_end = node.rchild
        cur_level_node += 1
        if node == cur_end:
            max_width = max(max_width, cur_level_node)
            cur_level_node = 0
            cur_end = next_end
    
    return max_width

