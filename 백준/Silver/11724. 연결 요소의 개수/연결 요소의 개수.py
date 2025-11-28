import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
dfs = [[] for _ in range(n)]
visited = [False] * n

for _ in range(m):
    u, v = map(int, input().split())
    dfs[u-1].append(v)
    dfs[v-1].append(u)

def DFS(idx):
    visited[idx] = True
    for i in dfs[idx]:
        if not visited[i-1]:
            DFS(i-1)

answer = 0
for i in range(n):
    if not visited[i]:
        answer += 1
        DFS(i)
print(answer)