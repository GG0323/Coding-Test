m = [[i]+list(input().split()) for i in range(int(input()))]

for i in sorted(m, key = lambda x: (int(x[1]), x[0])):
    print(f'{i[1]} {i[2]}')