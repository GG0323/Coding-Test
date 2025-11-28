n = int(input()); s = list(map(int, input().split())); t, p = map(int, input().split())
tc = sum([i//t + (1 if i%t != 0 else 0) for i in s])
print(f'{tc}\n{n//p} {n%p}')