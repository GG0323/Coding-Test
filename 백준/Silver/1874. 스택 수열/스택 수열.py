arr = [int(input()) for _ in range(int(input()))]
stack = []; num = 1; flag = True; ans = []

for idx, v in enumerate(arr):
    if v >= num:
        for i in range(num, v+1):
            stack.append(i)
            ans.append('+')
            num += 1
        stack.pop()
        ans.append('-')
    else:
        if v > stack.pop():
            flag = False
            break
        ans.append('-')

print('\n'.join(ans) if flag else 'NO')