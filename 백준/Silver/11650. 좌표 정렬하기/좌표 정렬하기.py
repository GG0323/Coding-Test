n = int(input())
for i in sorted([list(map(int, input().split())) for _ in range(n)]):
    print(f'{i[0]} {i[1]}')