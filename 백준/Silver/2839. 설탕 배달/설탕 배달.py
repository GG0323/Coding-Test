dp = [-1] * 5001
dp[3] = 1; dp[5] = 1
n = int(input())
for i in range(6, n+1):
    tmp = []
    if dp[i-3] != -1: tmp.append(dp[i-3])
    if dp[i-5] != -1: tmp.append(dp[i-5])
    dp[i] = min(tmp)+1 if tmp else -1

print(dp[n])