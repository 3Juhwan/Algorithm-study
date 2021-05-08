N, K = map(int, input().split())

dp = [[0 for _ in range(K)] for _ in range(N)]
for i in range(0, K):
    dp[0][i] = i + 1

for i in range(1, N):
    for j in range(0, K):
        dp[i][j] = sum(dp[i - 1][:j + 1])
        
print(dp[N - 1][K- 1] %  1000000000)