

def insert_sort(li):
    for i in range(1,len(li)):  # i表示摸到的牌的下标
        tmp = li[i]
        j = i - 1   #j 是指的手里的牌
        while li[j] > tmp and j>=0:
             li[j+1] = li[j]
             j = j - 1
        li[j+1] = tmp
    return li
li = [3,4,2,1,5,6,7,8,9]
print(insert_sort(li))