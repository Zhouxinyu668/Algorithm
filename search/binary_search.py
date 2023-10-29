
def search(list_1,val):
    left = 0
    right = len(list_1)-1
    mid = (left + right) // 2
    while right - left > 1:
        if list_1[mid] > val:
            right = mid
            mid = (left + right) // 2
        elif list_1[mid] < val:
            left = mid
            mid = (left + right) // 2
        elif list_1[mid] == val:
            return mid
    
    if list_1[right] == val:
        return right
    elif list_1[left] == val:
        return left
    else: 
        return None
    # return None

list_1 = [1,2,3,4,5,6,7]
val = 10
index = search(list_1,val)
print(index)

# a = 5 //2 
# b =5 % 2
# print(b)
# print(a)

def search_2(list_1,val):
    left = 0
    right = len(list_1)-1
    while right - left >= 0:
        mid = (left + right) // 2
        if list_1[mid] > val:
            right = mid-1
        elif list_1[mid] < val:
            left = mid+1
        else:
            return mid
    
    return None
index2 = search_2(list_1,val)
print(index2)