from itertools import permutations
s, k = input().split()
k = int(k)
perm = list(permutations(sorted(s), k))
for i in perm:
    string = ""
    for j in i:
        string = string + j
    print(string)
