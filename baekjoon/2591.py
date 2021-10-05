import sys
n = '0' + input()

dp = [[0] * len(n) for __ in range(2)]
dp[0][1] = 1
if len(n) == 2:
    print(1)
    sys.exit()
if n[2] != '0':
    dp[0][2] = 1    
if 10 <= int(n[1:3]) <= 34:
    dp[1][2] = 1

for i in range(3, len(n)):
    if n[i] != '0':
        dp[0][i] = dp[0][i-1] + dp[1][i-1]
    if 10 <= int(n[i-1: i+1]) <= 34:
        dp[1][i] = dp[0][i-2] + dp[1][i-2]

print(dp[0][-1] + dp[1][-1])