import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
sl = [0] * (n+1)

for i in range(1, n+1):
    sl[i] = sl[i-1] + arr[i-1]

for i in range(m):
    a, b = map(int, input().split())
    print(sl[b] - sl[a-1])