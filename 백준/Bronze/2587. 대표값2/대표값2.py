lst = sorted([int(input()) for _ in range(5)])
print('\n'.join([str(sum(lst)//5), str(lst[2])]))