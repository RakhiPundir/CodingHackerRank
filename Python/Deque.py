from collections import deque
d = deque()
n = int(input())
for i in range(n):
    command = input()
    l = list(command.split(" "))
    if(len(l)==1):
        if (l[0] == "pop"):
            d.pop()
        elif(l[0] == "popleft"):
            d.popleft()
    else:
        cmd = l[0]
        num = l[-1]
        if (cmd == "append"):
            d.append(num)
        elif(cmd == "appendleft"):
            d.appendleft(num)

for i in d:
    print(i, end=" ")
