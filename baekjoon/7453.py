import sys
input = sys.stdin.readline

n = int(input())
arr = [[] for __ in range(4)]
for __ in range(n):
    a, b, c, d = map(int, input().split())
    arr[0].append(a)
    arr[1].append(b)
    arr[2].append(c)
    arr[3].append(d)

dp = dict()

for i in range(n):
    for j in range(n):
        t = arr[0][i]+arr[1][j]
        if t in dp:
            dp[t] += 1
        else:
            dp[t] = 1

cnt = 0
for i in range(n):
    for j in range(n):
        t = -(arr[2][i]+arr[3][j])
        if t in dp:
            cnt += dp[t]
print(cnt)