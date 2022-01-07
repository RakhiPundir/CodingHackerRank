if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    summ=0
    list_marks = student_marks[query_name]
    for i in list_marks:
        summ = summ + i
    sumf = "{:.2f}".format(summ/3)
    print(sumf)
