from collections import deque
_, l = map(int, input().split())
arr = list(map(int, input().split()))
que = deque();ans = []

for idx, v in enumerate(arr):
    while que and que[-1][0] > v:
        que.pop()
    que.append((v, idx))

    if que[0][1] <= idx-l:
        que.popleft()
    ans.append(que[0][0])
    
print(*ans)