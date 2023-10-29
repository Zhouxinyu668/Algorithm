

def maxDistance(root):
    if head == None:
        return 0, 0
    
    left = maxDistance(root.left)
    right = maxDistance(root.right)
    height = max(left[0], right[0])
    maxdist = max(max(left[1],right[1]),left[0] + right[0] + 1)
    return maxdist, height
    
