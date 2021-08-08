dp = [0] * 10001

n = int(input())
dp[0] = 1
dp[2] = 1
dp[4] = 2

for i in range(6, n + 2, 2):
    for j in range(2, i + 2, 2):
        x, y = j - 2, i - j
        dp[i] += dp[x] * dp[y]
    dp[i] %= 987654321

print(dp[n])