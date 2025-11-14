n = int(input())
lst = sorted(list(map(int, input().split())))
answer = 0

for i in range(n):
    start, end = 0, n-1
    while start < end:
        tmp = lst[start] + lst[end]
        if tmp == lst[i]:
            if start != i and end != i:
                answer += 1
                break
            elif start == i:
                start += 1
            elif end == i:
                end -= 1
        elif tmp < lst[i]:
            start += 1
        else:
            end -= 1
            
print(answer)