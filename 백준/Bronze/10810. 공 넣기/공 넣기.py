n, k = map(int, input().split())
lst = ['0'] * n

for _ in range(k):
    i, j, k = map(int, input().split())
    for idx in range(i-1, j):
        lst[idx] = str(k)

print(' '.join(lst))