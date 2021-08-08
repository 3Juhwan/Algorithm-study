n = int(input())

dp = [0] * 1_000_001
dp[2] = 1

for i in range(3, n + 1):
    dp[i] = (i - 1) * (dp[i-1] + dp[i-2]) % 1_000_000_000

print(dp[n])