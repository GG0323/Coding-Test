origin = set(range(1,10001))
rmv = set()
for i in origin:
    for j in str(i):
        i += int(j)
    rmv.add(i)
for i in sorted(origin - rmv):
    print(i)