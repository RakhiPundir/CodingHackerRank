from itertools import product

a = input().split()
A = []
for i in a:
    A.append(int(i))

b = input().split()
B = []
for i in b:
    B.append(int(i))

pro = list(product(A, B))
for i in pro:
    print(i, end=" ")
