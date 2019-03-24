def aaddrf():
    a = 0
    b = []
    max = -1
    n = int(input())
    for i in range(n):
        b.append(int(input()))
    for i in range(n):
        if b[i] < b[i + 1]:
            a += 1
        else:
            continue
        if max < a:
            max = a
    print(max)
