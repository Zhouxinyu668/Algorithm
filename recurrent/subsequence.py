
from copy import copy

def process(char, i, res):
    if i == len(char):
        print(res)
        return
    
    resKeep = copy(res)
    resKeep.append(char[i])
    process(char, i+1, resKeep)
    resKeep = copy(res)
    process(char, i+1, resKeep)

def process2(char, i):
    if i == len(char):
        print(char)
        return
    process2(char, i+1)
    tmp = char[i]
    char[i] = 0
    process2(char, i+1)
    char[i] = tmp

#   char[i..]范围上，所有的字符都可以在i位置上，后续都去尝试
#   str[0.。i-1]范围上，是之前做的选择
#   把所有的字符串形成的全排列，加入到res中
def all_sort(char,i,res):
    if i == len(char):
        res.append(char)
    
    for j in range(i,len(char)):
        char[i], char[j] = char[j], char[i]
        process(char, i+1, res)
        char[i], char[j] = char[j], char[i]


char = ['a','b','c']
# process(char, 0, [])
# process2(char, 0)
res = []
all_sort(char,-1,res)

print(res)