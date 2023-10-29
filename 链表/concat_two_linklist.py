

if not pHead1:
    return pHead2
if not pHead2:
    return pHead1

dummyNode = ListNode(-1)
dummyNode.next = pHead1

pre = dummyNode
cur_1 = pHead1
cur_2 = pHead2

while cur_1 and cur_2:
    if cur_1.val < cur_2.val:
        pre = cur_1
        cur_1 = cur_1.next
    else:
        tmp = cur_2.next
        pre.next = cur_2
        cur_2.next = cur_1
        cur_2 = tmp
        pre = cur_1
        cur_1 = cur_1.next
if cur_1 is None:
    pre = cur_2
return dummyNode.next
        

        cur_2 = cur_2.next