


def getBSTSize(root):
    if root == None:
        return 0



def process(root):
    if root == None:
        return None, None, None, None
    
    left = process(root.lchild)
    right = process(root.rchild)
    min_val = root.val
    max_val = root.val
    if left[2] != None:
        min_val = min(min_val, left[2])
    if left[3] != None:
        max_val = max(max_val, left[3])

    if right[2] != None:
        min_val = min(min_val, right[2])
    if right[3] != None:
        max_val = max(max_val, right[3])
    
    maxSubBSTSize = 0
    if left[1] != None:
        maxSubBSTSize = left[1]
    if right[1] != None:
        maxSubBSTSize = max(maxSubBSTSize, right[1])
    
    isALLBST = False
    #和最初的根节点是否有关
    if (if left[0] == None else left[0]) and (if right[0] == None else right[0]) \
        and (if left[0] == None else left[3] < root.val ) and (if right[0] == None else right[2] > root.val):
        #整体是二叉搜索树
        if right[0] == None:
            right[1] = 0
        if right[0] == None:
            right[1] = 0
        maxSubBSTSize = left[1] + right[1] + 1
        isALLBST = True
    


    return isALLBST, maxSubBSTSize, min_val, max_val