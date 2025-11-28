num = [int(input()) for _ in range(10)]
count = 0
mod = []

for i in range(10):
    m = num[i] % 42
    if m not in mod:
        count += 1
        mod.append(m)

print(count)