# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
li = []
l1 = input().split()
for i in l1:
    i = int(i)
    li.append(i)
li = set(li)
m = int(input())
lj = []
l2 = input().split()
for i in l2:
    i = int(i)
    lj.append(i)
lj = set(lj)
print(len(set(li.union(lj))))
