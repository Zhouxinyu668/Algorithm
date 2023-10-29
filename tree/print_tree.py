from bitree import *


def getAfterNode(node):
    if node == None:
        return node
    if node.rchild:
        return getLeftMost(node.rchild)
    else:
        parent = node.parent
        while parent != None and parent.left != node:
            node = parent
            parent = node.parent

        return parent 


def getLeftMost(node):
    if node == None:
        return node
    
    while node.left:
        node = node.left
    return node
    