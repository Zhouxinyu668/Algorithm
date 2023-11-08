

# N为位置1-N
# rest为剩余步数
# cur为当前的位置
# p为目标位置
def robortWalk(N, cur, rest, p):
    if rest == 0:
        if cur == p:
            return 1
        else:
            return 0
    
    if cur == 1:
        return robortWalk(N, 2, rest-1, p)

    if cur == N:
        return robortWalk(N, N-1, rest-1, p)
    
    return robortWalk(N, cur+1, rest-1, p) + robortWalk(N, cur-1, rest-1, p)

