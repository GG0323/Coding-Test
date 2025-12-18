import sys
input = sys.stdin.readline
lst = [int(input()) for _ in range(int(input()))]
Max = max(lst) + 1
dp = [0] * Max
dp[1] = 1; dp[2] = 2; dp[3] = 4
for i in range(4, Max):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3])%1000000009
for i in lst:
    print(dp[i])