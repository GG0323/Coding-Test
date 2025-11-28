while True:
    p = input()
    if p == '0':
        break
    print('yes' if p == p[::-1] else 'no')