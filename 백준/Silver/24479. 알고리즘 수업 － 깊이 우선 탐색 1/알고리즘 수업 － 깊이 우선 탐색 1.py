import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m, start = map(int, input().split())
g = [[] for _ in range(n)]
visited = [False] * n
answer = [0] * n

for _ in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    g[a].append(b)
    g[b].append(a)
g = [sorted(i) for i in g]

def DFS(idx, count):
    visited[idx] = True
    answer[idx] = count
    count += 1
    for i in g[idx]:
        if not visited[i]:
            count = DFS(i, count)
    return count
DFS(start-1, 1)
print(*answer, sep='\n')