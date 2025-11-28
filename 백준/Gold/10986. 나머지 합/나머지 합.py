import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
sl = [0] * n
mod = [0] * m
result = 0

sl[0] = lst[0]
for i in range(1, n):
    sl[i] = sl[i-1] + lst[i]

for i in range(n):
    idx = sl[i] % m
    result += 1 if idx == 0 else 0
    mod[idx] += 1

for i in range(m):
    if mod[i] > 1:
        result += (mod[i] * (mod[i]-1) // 2)

print(result)