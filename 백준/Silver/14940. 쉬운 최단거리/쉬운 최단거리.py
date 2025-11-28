from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
origin = [list(map(int, input().split())) for _ in range(n)]
answer = [[-1] * m for _ in range(n)]
ij = [(-1, 0), (1, 0), (0, -1), (0, 1)]
start = 0
for i in range(n):
    for j in range(m):
        if origin[i][j] == 0:
            answer[i][j] = 0
        elif origin[i][j] == 2:
            start = (i, j)
            answer[i][j] = 0

q = deque([start])
while q:
    ci, cj = q.popleft()
    for h in range(4):
        i, j = ci + ij[h][0], cj + ij[h][1] 
        if i >= 0 and j >= 0 and i < n and j < m:
            if origin[i][j] == 1 and answer[i][j] == -1:
                answer[i][j] = answer[ci][cj] + 1
                q.append((i, j))
for i in answer:
    print(*i)