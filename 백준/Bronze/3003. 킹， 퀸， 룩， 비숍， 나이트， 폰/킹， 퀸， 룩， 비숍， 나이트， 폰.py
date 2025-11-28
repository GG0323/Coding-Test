p = [1, 1, 2, 2, 2, 8]
n = list(map(int, input().split()))
print(' '.join([str(p[i] - n[i]) for i in range(6)]))