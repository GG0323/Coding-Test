n = int(input())
result = 1
f = False
while result != n:
    if sum([int(i) for i in str(result)]) + result == n:
        f = True
        break
    result += 1
    
print(result if f else 0)