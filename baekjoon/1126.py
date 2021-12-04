import sys
input = sys.stdin.readline
TOP = 500_001


n = int(input())
dp = [-1]*TOP
dp[0] = 0

for x in map(int, input().split()):
    t = dp[:]
    for i in range(0, TOP-x):
        if dp[i] != -1:
            t[i+x] = max(t[i+x], dp[i+x], dp[i])
            if i >= x:
                t[i-x] = max(t[i-x], dp[i-x], x+dp[i])
            else:
                t[x-i] = max(t[x-i], dp[x-i], i+dp[i])
    dp = t

print(dp[0] if dp[0] else -1)