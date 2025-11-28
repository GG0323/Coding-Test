lst = []
for _ in range(int(input())):
    a = int(input())
    if a == 0:
        lst.pop()
        continue
    lst.append(a)
print(sum(lst))