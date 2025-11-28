from collections import deque
n, m = map(int, input().split())
lst = [[int(i) for i in input()] for _ in range(n)]
visited = [[False]*m for _ in range(n)]
ij = [(-1, 0), (1, 0), (0, -1), (0, 1)]
q = deque([(0, 0)]); visited[0][0] = True
while q:
    ci, cj = q.popleft()
    for h in range(4):
        i, j = ci + ij[h][0], cj + ij[h][1]
        if i >= 0 and j >= 0 and i < n and j < m:
            if lst[i][j] and not visited[i][j]:
                visited[i][j] = True
                lst[i][j] = lst[ci][cj] + 1
                q.append((i, j))
print(lst[n-1][m-1])