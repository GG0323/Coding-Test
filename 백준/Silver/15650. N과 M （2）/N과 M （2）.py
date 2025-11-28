n, m = map(int, input().split())

def back(num, level, start):
    if level == m:
        print(num.rstrip())
        return
    for i in range(start, n+1):
        i = str(i)
        if i in num:
            continue
        back(num + i + ' ', level + 1, int(i))

back('', 0, 1)