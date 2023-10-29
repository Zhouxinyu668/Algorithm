class Node:
    def __init__(self,item):
        self.item = item
        self.next = None


a = Node(0)
b = Node(1)
c = Node(2)
a.next = b
b.next = c

# 将4插入到0和1之间
d = Node(4)
d.next = b
a.next = d


def print_linklist(li):
    while li:
        print(li.item,end=',')
        li = li.next
print_linklist(a)

#删除4节点
a.next = b
del d

print_linklist(a)