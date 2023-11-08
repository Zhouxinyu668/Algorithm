
import time

p = [0,1, 5, 8, 9, 10, 17, 17, 20, 21, 23, 25, 26, 27, 28,29]
#递归版本
def cur_rod_recurision(p, n):
    if n == 0:
        return 0
    else:
        res = p[n]
        for i in range(1,(n // 2)):
            res = max(res, p[i] + + cur_rod_recurision(p, n - i))
        return res

def cur_rod_recurision_2(p, n):
    if n == 0:
        return p[0]
    else:
        res = 0
        for i in range(1, n+1):
            res = max(res, p[i] + cur_rod_recurision_2(p, n - i))
        return res

def dp_cur_rod(p,n):
    r = [0]
    for i in range(1, n+1):
        res = 0
        for j in range(1, i+1):
            res = max(res,p[j] + r[i-j])
        r.append(res)
    return r[n]

start = time.time()
print(cur_rod_recurision(p, 15))
end = time.time()
print(end- start)

start = time.time()
print(cur_rod_recurision_2(p, 15))
end = time.time()
print(end- start)


start = time.time()
print(dp_cur_rod(p, 15))
end = time.time()
print(end- start)