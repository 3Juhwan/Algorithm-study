import sys
input = sys.stdin.readline

N = int(input())
graph = []
for __ in range(N):
    graph.append(list(map(int, input().split())))

dp = [[0] * N for __ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if not dp[i][j] or not graph[i][j]:
            continue

        d1, d2 = i + graph[i][j], j + graph[i][j]
        if d1 < N:
            dp[d1][j] += dp[i][j]
        if d2 < N:
            dp[i][d2] += dp[i][j]

print(dp[-1][-1])