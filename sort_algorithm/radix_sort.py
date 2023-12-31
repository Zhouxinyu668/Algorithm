

#时间复杂度O(kn)

def radix_sort(li):
    max_num = max(li)   #最大值
    it = 0
    while 10**it <= max_num:
        buckets = [[] for _ in range(10)]
        for var in li:
            digit = (var//10**it) % 10

            buckets[digit].append(var)
        #分桶完成
        li.clear()
        for buc in buckets:
            li.extend(buc)
        #把数重新写回li
        it += 1
    

import random
li = list(range(10000))
random.shuffle(li)
radix_sort(li)
