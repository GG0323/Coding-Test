n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))
result = []
def back(lev, num, idx):
    if lev == m:
        if num.rstrip() not in result:
            result.append(num.rstrip())
        return
    for i in range(idx, len(lst)):
        if str(lst[i]) not in num:
            back(lev+1, num + str(lst[i]) + ' ', i+1)
back(0, '', 0)

print(*result, sep='\n')