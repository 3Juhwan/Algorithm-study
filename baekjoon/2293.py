N, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

dp = [0] * (K + 1)
dp[0] = 1

for x in arr:
    for i in range(1, K + 1):
        if i - x >= 0:
            dp[i] += dp[i - x]

print(dp[K])