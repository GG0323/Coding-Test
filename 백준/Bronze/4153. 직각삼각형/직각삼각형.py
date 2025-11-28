while True:
    t = list(map(int, input().split()))
    if t[0] == 0 and t[1] == 0 and t[2] == 0:
        break
    hyp = max(t); t.remove(hyp)
    print('right' if t[0]**2 + t[1]**2 == hyp**2 else 'wrong')