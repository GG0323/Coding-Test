for _ in range(int(input())):
    ox = input()
    result = 0
    tmp = 1
    for i in ox:
        if i == 'X':
            tmp = 1
            continue
        result += tmp
        tmp += 1
    print(result)