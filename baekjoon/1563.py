n = int(input())
dp = [[[0] * 3 for __ in range(2)] for __ in range(n+1)]
dp[1] = [[1, 1, 0], [1, 0, 0]]

for i in range(1, n):
    dp[i+1][0][0] += sum(dp[i][0])
    dp[i+1][0][1] += dp[i][0][0]
    dp[i+1][0][2] += dp[i][0][1]
    dp[i+1][1][0] += sum(map(sum, dp[i]))
    dp[i+1][1][1] += dp[i][1][0]
    dp[i+1][1][2] += dp[i][1][1]
    dp[i+1] = [list(map(lambda x: x % 1_000_000, x)) for x in dp[i+1]]

print(sum(map(sum, dp[n])) % 1_000_000)