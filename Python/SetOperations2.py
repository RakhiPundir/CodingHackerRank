n = int(input())
s = set(map(int, input().split()))
m = int(input())
for i in range(m):
    command = input()
    if command == "pop":
        s.pop()
    else:   
        c = list(command.split(" "))
        comm = c[0]
        num = int(c[-1]) 
        if comm == "remove":
            s.remove(num)
        elif comm == "discard":
            s.discard(num)
print(sum(list(s)))
