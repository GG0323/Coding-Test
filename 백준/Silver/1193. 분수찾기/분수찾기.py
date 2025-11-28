n = int(input()); line = 1

while n > line:
    n -= line
    line += 1

if line % 2: a, b = line - n + 1, n
else: a, b = n, line - n + 1
print(f'{a}/{b}')