import sys
m, n = map(int, input().split())
prime = [i for i in range(n+1)]
prime[0] = prime[1] = 0

for i in range(2, int(n**0.5)+1):
    if not prime[i]:
        continue
    for j in range(i*i, n+1, i):
        prime[j] = 0

for i in range(m, n+1):
    if prime[i]:
        sys.stdout.write(f'{prime[i]}\n')