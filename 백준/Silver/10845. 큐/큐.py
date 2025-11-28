from collections import deque
import sys

input = sys.stdin.readline
d = deque()

for _ in range(int(input())):
    n = input()
    if 'push' in n :
        d.append(int(n.split()[1]))
    elif 'pop' in n :
        print(d.popleft() if d else -1)
    elif 'size' in n :
        print(len(d))
    elif 'empty' in n:
        print(int(bool(not d)))
    elif 'front' in n :
        print(d[0] if d else -1)
    else:
        print(d[-1] if d else -1)