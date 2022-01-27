from collections import Counter
x = int(input())
shoe_sizes_list = list(map(int, input().split()))
count = Counter(shoe_sizes_list)
money = 0
n = int(input())
for i in range(n):
    a, b = input().split()
    a = int(a)
    b = int(b)
    if(count[a]==0):
        continue

    elif (a not in shoe_sizes_list):
        continue
    
    else:
        count[a] -= 1
        money = money + b
        
print(money)
