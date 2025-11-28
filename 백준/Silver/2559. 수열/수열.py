n, k = map(int, input().split())
tmp = list(map(int, input().split()))
sl = [0] * (n+1)
result = [0] * (n-k+1)

for i in range(1, n+1):
    sl[i] = sl[i-1] + tmp[i - 1]

for i in range(n-k+1):
    result[i] = sl[k] - sl[i]
    k += 1

print(max(result))