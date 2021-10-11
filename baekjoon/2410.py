n = int(input())
dp = [0, 1, 2]

for i in range(3, n+1):
    if i%2:
        dp.append(dp[i-1])
    else:
        dp.append((dp[i-1] + dp[i//2]) % int(1e9))

print(dp[n])