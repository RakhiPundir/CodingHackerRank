from itertools import combinations
s, k = input().split()
k = int(k)
perm = []
for size in range(1,k+1):
    comb = list(combinations(sorted(s), size))
    perm.append(comb)
for i in perm:
    
    for j in i:
        string = ""
        for k in j:
            string = string + k
        print(string)
