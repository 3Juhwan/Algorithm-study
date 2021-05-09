import sys

N = int(input())
charge = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
dp = [0 for _ in range(N + 1)]
dp[1] = charge[1]

for i in range(1, N + 1):
    dp[i] = charge[i]
    for j in range(1, i // 2 + 1):
        dp[i] = max(dp[i], charge[j] + dp[i - j])

print(dp[N])