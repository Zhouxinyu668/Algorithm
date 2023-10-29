
class Node:
    def __init__(self,item):
        self.item = item
        self.next = None


#头插法
def create_Linklist(li):
    head = Node(li[0])
    for element in li[1:]:
        node = Node(element)
        node.next = head
        head = node
    return head


#尾插法
def create_Linklist_tail(li):
    head = Node(li[0])
    tail = Node(li[0])
    # head.next = tail
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head


#传入头节点
def iter_linklist(li):
    while li:
        print(li.item,end=',')
        li = li.next
