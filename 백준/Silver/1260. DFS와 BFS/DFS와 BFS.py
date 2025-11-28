from collections import deque
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m, start = map(int, input().split())
g = [[] for _ in range(n)]
stamp = deque()
dfs, bfs = [], []

for _ in range(m):
    a, b = map(int, input().split())
    g[a-1].append(b)
    g[b-1].append(a)
g = [sorted(i) for i in g]

def DFS(idx):
    visited[idx] = True
    dfs.append(idx+1)
    for i in g[idx]:
        if not visited[i-1]:
            DFS(i-1)

def BFS(idx):
    visited[idx] = True
    bfs.append(idx+1)
    for i in g[idx]:
        if not visited[i-1]:
            visited[i-1] = True
            stamp.appendleft(i)
    while stamp:
        BFS(stamp.pop()-1)

visited = [False] * n
DFS(start-1)
visited = [False] * n
BFS(start-1)

print(*dfs)
print(*bfs)