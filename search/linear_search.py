
def search(list_1,val):
    for index, v in enumerate(list_1):
        if val == v:
            return index
    return None

list_1 = [1,2,3]
val = 2
index = search(list_1,val)
print(index)