import sys
input = sys.stdin.readline

n = int(input()) + 1
num = list(map(int, input().split()))
sl = [0] * (n)
result = []

for i in range(1, n):
    sl[i] = sl[i-1] + num[i-1]

for i in range(int(input())):
    a, b = map(int, input().split())
    print(sl[b] - sl[a - 1])