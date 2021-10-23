import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[0]*301 for __ in range(301)]
for __ in range(k):
    a, b, c = map(int, input().split())
    if a < b:
        if graph[a][b]:
            graph[a][b] = max(graph[a][b], c)
        else:
            graph[a][b] = c

dp = [[0] * (m+1) for __ in range(301)]

for i in range(1, 301):
    if graph[1][i]:
        dp[i][2] = graph[1][i]

for i in range(1, 301):
    for j in range(1, 301):
        for k in range(3, m+1):
            if graph[i][j] and dp[i][k-1]:
                dp[j][k] = max(dp[j][k], dp[i][k-1]+graph[i][j])

print(max(dp[n]))