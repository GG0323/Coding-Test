n, m = map(int, input().split())

def back(num, level, start):
    if level == m:
        print(num.rstrip())
        return
    for i in range(start, n+1):
        back(num + str(i) + ' ', level + 1, i)

back('', 0, 1)