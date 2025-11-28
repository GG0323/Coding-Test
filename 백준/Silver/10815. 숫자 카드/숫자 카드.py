input()
n = sorted(list(map(int, input().split())))
input()
m = list(map(int, input().split()))
result = []

def bs(start, end, f):
    if start > end:
        return '0'
    
    mid = (start + end) // 2
    return '1' if n[mid] == f else bs(start, mid-1, f) if n[mid] > f else bs(mid+1, end, f)

for i in m:
    result.append(bs(0, len(n)-1, i))

print(' '.join(result))