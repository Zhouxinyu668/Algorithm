

# 如果返回-1认为没有方案
# index之后的货产生多少价值
def getMaxValue(w, v, index, alreadyW, bag):
    if alreadyW > bag:
        return -1
    if index == len(w):
        return 0
    p1 = getMaxValue(w, v, index+1, alreadyW, bag)
    p2next = getMaxValue(w, v, index+1, alreadyW + w[index], bag)

    p2 = -1
    if p2next != -1:
        p2 = v[index] + p2next
    return max(p1, p2)

# 只剩下rest的空间
# index货物自由选，不能超过rest的空间
# 返回能够获得的最大价值
def maxValue(w, v, index, rest):
    if rest <= 0:
        return 0
    if index == len(w):
        return 0
    
    p1 = maxValue(w, v, index+1, rest)
    p2 = -1
    p2next = maxValue(w, v, index+1, rest-w[index])
    if p2next != -1:
        p2 = v[index] + p2next
    return max(p1, p2)

maxValue(w, v, 0, bag)
    