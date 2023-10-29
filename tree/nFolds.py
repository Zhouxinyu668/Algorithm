


def printProcess(i, n, down):
    if i > n:
        return
    printProcess(i+1, n, True)
    print("凹" if down else "凸")
    printProcess(i+1, n, False)

printProcess(1,3, True)