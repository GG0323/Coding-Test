n, m = map(int, input().split())
bk = [i for i in range(1, n+1)]
for i in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    bk[a], bk[b] = bk[b], bk[a]

print(' '.join([str(i) for i in bk]))