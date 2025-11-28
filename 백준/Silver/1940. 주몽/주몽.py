n = int(input()); m = int(input())
lst = sorted(list(map(int, input().split())))
answer, start, end = 0, 0, n-1
while start < end:
    tot = lst[start] + lst[end]
    if tot > m:
        end -= 1
    elif tot < m:
        start += 1
    else:
        answer += 1
        start += 1
        end -= 1
print(answer)