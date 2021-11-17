t = int(input())
dp = [[0]*15 for __ in range(15)]

for i in range(15):
    dp[0][i] = i

for i in range(1, 15):
    for j in range(1, 15):
        dp[i][j] = sum(dp[i-1][:j+1])

for __ in range(t):
    a = int(input())
    b = int(input())
    print(dp[a][b])