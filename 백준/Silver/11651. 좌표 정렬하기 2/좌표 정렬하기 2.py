n = int(input())
for i, j in sorted([list(map(int, input().split())) for _ in range(n)], key = lambda x: (x[1], x[0])):
    print(f'{i} {j}')