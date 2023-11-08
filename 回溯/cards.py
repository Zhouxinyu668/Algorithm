

def cards_0(arr, l, r):
    if l == r:
        return arr[l]
    
    left = arr[l] + cards_1(arr, l+1, r)
    right = arr[r] + cards_1(arr, l, r-1)
    return max(left, right)

def cards_1(arr, l, r):
    if l==r:
        return 0
    left = cards_0(arr, l+1 ,r)
    right = cards_0(arr, l, r-1)
    return min(left,right)

def win1(arr):
    if len(arr) == 0:
        return 0
    return max(cards_0(arr, 0, len(arr)-1),cards_1(arr, 0, len(arr)-1))

arr = [1,20,40,2,40,60]

cards_point = win1(arr)
print(cards_point)