

str1 = 'abcbdab'
str2 = 'bdcaba'

res = [[0 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]
source = [[0 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]
def lcs(str1, str2, res):
    # str_list = []
    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            if str1[i-1] == str2[j-1]:  # i 和 j 位置的字符匹配的时候，来自于左上方+1
                res[i][j] = res[i-1][j-1] + 1
                source[i][j] = 2
            
            # res[i][j] = max(res[i-1][j],res[i][j-1])
            elif res[i-1][j] >= res[i][j-1]:
                res[i][j] = res[i-1][j]
                source[i][j] = 3
            else:
                res[i][j] = res[i][j-1]
                source[i][j] = 1
    
    return res[-1][-1]

def lcs_path(str1, str2, source):
    path = []
    i = len(str1)
    j = len(str2)
    while i > 0 and j > 0:
        num = source[i][j]
        # print(num)
        if num == 2:  #来自左上方
            path.append(str1[i-1])
            i -= 1
            j -= 1
        if num == 1:    #来自左方
            j -= 1
        if num == 3:    #来自上方
            i -= 1
    return path


# print(len(res))
value = lcs(str1, str2, res)
print(value)
# print(source)
path = lcs_path(str1, str2, source)
print(''.join(reversed(path)))