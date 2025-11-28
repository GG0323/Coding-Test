import sys
input = sys.stdin.readline

_, m = map(int, input().split())
num = list(map(int, input().split()))
tot = [0]
tmp = 0

for i in num:
    tmp += i
    tot.append(tmp)

for i in range(m):
    s, e = map(int, input().split())
    print(tot[e] - tot[s - 1])