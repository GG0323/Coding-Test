n, m = map(int, input().split())
arr = [str(i) for i in range(1, n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    tmp = arr[i-1:j][::-1]
    arr[i-1:j] = tmp

print(' '.join(arr))