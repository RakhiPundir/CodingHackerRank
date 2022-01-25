def average(array):
    # your code goes here
    distinct_elements = set(array)
    n = len(distinct_elements)
    s = 0
    for i in distinct_elements:
        s = s + i
    avg = float(s/n)
    return(round(avg, 3))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
