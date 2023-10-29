
def bubble__sort(list_1):
    for i in range(len(list_1)-1):
        for j in range(len(list_1)-i-1):
            exchange = False   #如果
            if list_1[j] > list_1[j+1]:
                list_1[j], list_1[j+1] = list_1[j+1],list_1[j]
                exchange = True
        if not exchange:
            return list_1
    return list_1

list1 = [1,5,4,3,8,7,2,6,9]
new_list = bubble__sort(list_1=list1)
print(new_list)