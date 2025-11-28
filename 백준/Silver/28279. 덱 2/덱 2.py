import sys
from collections import deque
input = sys.stdin.readline
d = deque()

for _ in range(int(input())):
    op = input()
    if '1' == op[0]:
        d.appendleft(op.split()[-1])
    elif '2' == op[0]:
        d.append(op.split()[-1])
    elif '3' == op[0]:
        print(d.popleft() if d else -1)
    elif '4' == op[0]:
        print(d.pop() if d else -1)
    elif '5' == op[0]:
        print(len(d))
    elif '6' == op[0]:
        print(int(bool(not d)))
    elif '7' == op[0]:
        print(d[0] if d else -1)
    else:
        print(d[-1] if d else -1)