
def hanoi(n,a,b,c):
    if n > 0:
        hanoi(n-1,a,c,b)
        print("moving from  %s to %s"%(a,c))
        hanoi(n-1,b,a,c)
        # print()
# hanoi(3,'a','b','c')


def hanoi_clear(i, start, end, other):
    if i == 1:
        print("Move 1 from " + start + " to " + end)
    else:
        hanoi_clear(i-1, start, other, end)
        print("Move " + str(i) + " from " + start + " to " + end)
        hanoi_clear(i-1, other, end, start)
hanoi_clear(3, "左", "右", "中")
