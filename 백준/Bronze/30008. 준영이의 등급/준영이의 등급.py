n, _ = map(int, input().split())
print(' '.join(list(map(lambda y: '9' if y>96 else '8' if y>89 else '7' if y>77 else '6' if y>60 else '5' if y>40 else '4' if y>23 else '3' if y>11 else '2' if y>4 else '1', (list(map(lambda x: x*100//n, list(map(int, input().split())))))
))))