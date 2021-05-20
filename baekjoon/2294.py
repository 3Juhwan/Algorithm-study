INF = int(1e9)

N, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
dp = [INF] * (K + 1)
dp[0] = 0

for x in arr:
    if x <= K:
        dp[x] = 1

for  i in range(1, K + 1):
    for x in arr:
        if i - x >= 0:
            dp[i] = min(dp[i], dp[i - x] + 1)

if dp[K] == INF:
    print(-1)
else:
    print(dp[K])