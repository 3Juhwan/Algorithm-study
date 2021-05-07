N, M = map(int, input().split())
db = []
for _ in range(N):
    db.append(list(map(int, input().split())))

dp = [[0 for _ in range(M)] for _ in range(N)]

# shift
dx = [0, -1, -1]
dy = [-1, 0, -1]

for x in range(N):
    for y in range(M):
        dp[x][y] = db[x][y]

        for i in range(3):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0:
                continue

            dp[x][y] = max(dp[x][y], db[x][y] + dp[nx][ny])

print(dp[N - 1][M - 1])