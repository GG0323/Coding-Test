import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = [list(map(int, input().split())) for _ in range(n)]
sl = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        sl[i][j] = num[i-1][j-1] + sl[i-1][j] + sl[i][j-1] - sl[i-1][j-1]

for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    print(sl[x][y] + sl[i-1][j-1] - sl[i-1][y] - sl[x][j-1])