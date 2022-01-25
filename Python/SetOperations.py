nM = int(input())
rM = input()
lis = rM.split()
M = set(lis)
nN = int(input())
rN = input()
lis = rN.split()
N = set(lis)
un = N.union(M)
inter = M.intersection(N)
diff = un.difference(inter)

s = []
for i in diff:
    s.append(int(i))

for i in sorted(s):
    print(i)
