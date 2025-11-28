from collections import deque
n = deque([str(i) for i in range(1, int(input())+1)])
result = []
while len(n) > 1:
    result.append(n.popleft())
    tmp = n.popleft()
    n.append(tmp)
result.append(n.pop())
print(*result)