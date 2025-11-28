from math import gcd
n = int(input())
ring = list(map(int, input().split()))
for i in range(1, n):
    g = gcd(ring[0], ring[i])
    print(f'{ring[0]//g}/{ring[i]//g}')