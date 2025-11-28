for _ in range(int(input())):
    stack = []
    for i in input():
        if i == '(':
            stack.append(1)
        else:
            if stack:
                stack.pop()
            else:
                stack.append(1)
                break
    print('YES' if not stack else 'NO')