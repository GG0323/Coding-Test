n = int(input())
for i in sorted(set([input() for _ in range(n)]), key = lambda x: (len(x), x)):
    print(i)