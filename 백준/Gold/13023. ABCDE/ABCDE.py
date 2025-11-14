import sys
input = sys.stdin.readline
n, m = map(int, input().split())
g = [[] for _ in range(n)]
visited = [False] * n
answer = False

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

def DFS(n, lev):
    if lev == 5:
        return True
    visited[n] = True
    for i in g[n]:
        if not visited[i]:
            if DFS(i, lev+1):
                return True
    visited[n] = False
    return False

for i in range(n):
    if DFS(i,1):
        answer = True
        break

print(int(answer))