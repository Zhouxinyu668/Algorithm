

# i 是当前来到的行
# n是所有的行数
# i-1 都存在record里
def nQueen(i, record, n):
    if i == n:
        return 1
    res = 0

    for j in range(n):
        if isValid(record, i, j):
            record[i] = j
            res += nQueen(i+1, record, n)
            record[i] = -1
    return res


def isValid(record, i, j):
    for k in range(i):
        if j == record[k] or abs(record[k] - j) == abs(i - k):
            return False
    
    return True



n = 8
print(nQueen(0, [-1 for _ in range(n)], n))