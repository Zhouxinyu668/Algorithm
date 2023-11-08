
def sift(li,low,high):
    # li 列表
    # low 堆的根节点位置
    # high 堆的最后一个元素位置
    i = low     #i最开始指向根节点
    j = 2 * i + 1   #j开始是左孩子
    tmp = li[low]       #堆顶
    while j <= high:
        if j + 1<= high and li[j+1] > li[j]:        #如果右孩子有且比较大
            j = j + 1  #j指向右孩子
        if tmp < li[j]:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            li[i] = tmp
            break
    else:
        li[i] = tmp

# def topk(li,k):
#     heap = li[0:k]
#     for i in range((k-2)//2,-1,-1):
#         sift(heap,i,k-1) #建堆
#     for i in range(k,len(li)-1):
#         if li[k] > heap[0]:
#             heap[0] = li[k]
#             sift(heap,0,k-1)
#     print(heap)
#         #遍历列表中剩下的元素
#     for i in range(k-1,-1,-1):
#         heap[i],heap[0] = heap[0], heap[i]
#         sift(heap,0,i-1)
#     return heap


def top_small_k(li,k):
    heap = li[0:k]
    for i in range((k-2)//2,-1,-1):
        sift(heap,i,k-1)
    for i in range(k,len(li)-1):
        if li[i] < heap[0]:
            heap[0] = li[i]
            sift(heap,0,k-1)
    # for i in range(k-1,-1,-1):
    #     if li[i]
    return heap 
 
li = [i for i in range(10)]
import random
random.shuffle(li)
# print(li)
# print(top_small_k(li,2))
    


def head_sort(li):
    n = len(li)
    print(n)
    for i in range((n-2)//2,-1,-1):
        print(i)

        # i 表示建堆的时候调整的部分的根的下标
        sift(li,i,n-1)
    print(li)
    for i in range(n-1,-1,-1):
        # i 一直指的是当前堆的最后一个
        li[i],li[0] = li[0],li[i]
        sift(li,0,i-1)
    print(li)
                

# li = [i for i in range(100)]
# import random
# random.shuffle(li)
print(li)
head_sort(li)


