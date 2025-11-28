import sys
from collections import deque
input = sys.stdin.readline
queue = deque()

for i in range(int(input())):
    op = input()
    if 'push' in op:
        queue.append(op.split()[-1])
    elif 'pop' in op:
        print(f'{queue.popleft() if queue else -1}')
    elif 'size' in op:
        print(f'{len(queue)}')
    elif 'empty' in op:
        print(f'{int(bool(not queue))}')
    elif 'front' in op:
        print(f'{queue[0] if queue else -1}')
    else:
        print(f'{queue[-1] if queue else -1}')