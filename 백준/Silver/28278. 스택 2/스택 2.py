import sys
input = sys.stdin.readline
stack = []

for i in range(int(input())):
    op = input()
    if '1' == op[0]:
        stack.append(op.split()[-1])
    elif '2' == op[0]:
        print(f'{stack.pop() if stack else -1}')
    elif '3' == op[0]:
        print(f'{len(stack)}')
    elif '4' == op[0]:
        print(f'{int(bool(not stack))}')
    else:
        print(f'{stack[-1] if stack else -1}')