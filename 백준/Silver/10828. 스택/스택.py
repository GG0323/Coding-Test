import sys
input = sys.stdin.readline

stack = []
for _ in range(int(input())):
    command = input()
    if 'push' in command:
        stack.append(command.split()[1])
    elif 'pop' in command:
        print(stack.pop() if stack else -1)
    elif 'size' in command:
        print(len(stack))
    elif 'empty' in command:
        print(int(bool(not stack)))
    else:
        print(stack[-1] if stack else -1)