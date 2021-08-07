import sys
input = sys.stdin.readline

INF = 1001

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = int(1e9)

for i in range(3):
    dp = [[0] * 3 for _ in range(n)]
    dp[0][0], dp[0][1], dp[0][2] = arr[0][0], arr[0][1], arr[0][2]
    dp[0][i] = INF
    
    for j in range(1, n):
        dp[j][0] = arr[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = arr[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = arr[j][2] + min(dp[j-1][0], dp[j-1][1])
    
    result = min(result, dp[-1][i])

print(result)