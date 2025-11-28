n = list(map(int, input().split()))
print('ascending' if n == sorted(n) else 'descending' if n == sorted(n, reverse=True) else 'mixed')