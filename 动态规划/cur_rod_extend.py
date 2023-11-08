from collections import deque

def dp_cur_rod(p,n):
    r = [0]
    for i in range(1, n+1):
        res = 0
        for j in range(1, i+1):
            res = max(res,p[j] + r[i-j])
        r.append(res)
    return r[n]
# p = [0,1, 5, 8, 9, 10, 17, 17, 20, 21, 23, 25, 26, 27, 28,29]
p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

def cur_rod_extend(p, n):
    r = [0]
    s = [0]
    for i in range(1, n+1):
        res = 0
        max_length = 0
        for j in range(1, i+1):
            if p[j] + r[i-j] > res:
                max_length = j
                res = p[j] + r[i-j]
        s.append(max_length)
        r.append(res)
    return r[n], s
# def cur_rod_solution(n, s):
#     q = deque()
#     q.append(n-s[n])
#     q.append(s[n])
#     res = []
#     while len(q) > 0:
#         val = q.pop()
#         if val == 0:
#             return res
#         if s[val] == val:
#             res.append(val)
#         else:
#             q.append(s[val] - val)
#             q.append(s[val])
#     return res
def cur_rod_solution(n, s):
    ans = []
    while n > 0:
        ans.append(s[n])
        n -= s[n]
    return ans
    
value, s = cur_rod_extend(p, 10)
print(s)
res = cur_rod_solution(5,s)
print(res)
# target = s[n]
# res = []
# while target > 0:
#     res.append()