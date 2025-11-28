n = int(input())
start, end, count, sm = 1, 1, 1, 1
while end != n:
    if sm == n:
        count += 1
        end += 1
        sm += end
    elif sm > n:
        sm -= start
        start += 1
    else:
        end += 1
        sm += end
print(count)