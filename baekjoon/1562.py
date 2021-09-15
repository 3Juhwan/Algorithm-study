MOD = 1_000_000_000
NUM = 1 << 10

n = int(input())
dp = [[[0] * NUM for __ in range(10)] for __ in range(n+1)]
for i in range(1, 10):
    dp[0][i][1 << i] = 1

for i in range(n):
    for k in range(NUM):
        dp[i+1][1][k | (1 << 1)] = (dp[i+1][1][k | (1 << 1)] + dp[i][0][k]) % MOD
    for j in range(1, 9):
        for k in range(NUM):
            dp[i+1][j-1][k | (1 << j-1)] = (dp[i+1][j-1][k | (1 << j-1)] + dp[i][j][k]) % MOD
            dp[i+1][j+1][k | (1 << j+1)] = (dp[i+1][j+1][k | (1 << j+1)] + dp[i][j][k]) % MOD
    for k in range(NUM):
        dp[i+1][8][k | (1 << 8)] = (dp[i+1][8][k | (1 << 8)] + dp[i][9][k]) % MOD

print(sum([dp[n-1][i][NUM-1] for i in range(10)]) % MOD)