n = int(input()); lst =  sorted(list(map(int, input().split())))
print(f'{sum(lst[:n//2])} {sum(lst[n//2:])}')