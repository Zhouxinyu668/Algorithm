def select_sort_sample(li):
    new_li = []
    for i in range(li):
        min_val = min(li)
        new_li.append(min_val)
        li.remove(min_val)
    return new_li


def select_sort(li):
    for i in range(len(li)-1):
        min_loc = i
        flag = False
        for j in range(i+1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
                flag = True
        if flag == False:
            return li
        li[i],li[min_loc] = li[min_loc], li[i]
    return li
li = [3,4,2,1,5,6,7,8,9]
print(select_sort(li))


