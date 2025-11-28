n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))

def back(arr):
    if len(arr) == m:
        print(*arr)
        return
    for i in lst:
        if i in arr:
            continue
        arr.append(i)
        back(arr)
        arr.pop()

back([])