n, m = map(int, input().split())

def back(num, lev):
    if lev == m:
        print(num.strip())
        return
    for i in range(1, n + 1):
        back(num + str(i) + ' ', lev+1)

back('', 0)