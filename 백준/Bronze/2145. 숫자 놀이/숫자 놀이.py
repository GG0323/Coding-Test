def sn(num_list):
    return sum([int(i) for i in num_list])

while True:
    n = input()
    if n == '0':
        break
    result = sn(n)
    while result // 10:
        result = sn(str(result))
    print(result)