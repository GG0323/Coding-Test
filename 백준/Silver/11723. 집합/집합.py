import sys
input = sys.stdin.readline
All = {i for i in range(1, 21)}
S = set()

for _ in range(int(input())):
    op = input().split()
    if len(op) == 2: n = int(op[1])
    
    if op[0] == 'add': S.add(n)
    elif op[0] == 'remove':
        if n in S: S.discard(n)
    elif op[0] == 'check': sys.stdout.write(f'{int(n in S)}\n')
    elif op[0] == 'toggle':
        S.discard(n) if n in S else S.add(n)
    elif op[0] == 'all': S.update(All)
    else: S.clear()