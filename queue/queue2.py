from collections import deque

# q = deque()
# q.append(1)  #队尾进队
# q.popleft()  #队首出队


# # 用于双向队列的
# q.appendleft(2) #队首进队
# q.pop()         #队尾出队

def tail(n):
    with open('D:\\vscode文件\算法题\queue\\test.txt','r') as t:
        q = deque(t,n)
        return q

for line in tail(5):
    print(line,end='')