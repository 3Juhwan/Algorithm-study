import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for __ in range(n)]

dp = [0] * (n+1)

for i in range(n):
    t, p = arr[i]
    if i+t > n: continue
    dp[i] = max(dp[i], dp[i-1])
    dp[i+t] = max(dp[i+t], dp[i]+p)

print(max(dp))