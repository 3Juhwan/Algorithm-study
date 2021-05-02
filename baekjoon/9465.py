# New Codes
T = int(input())
for _ in range(T):
    N = int(input())
    dp = []
    dp.append(list(map(int, input().split())))
    dp.append(list(map(int, input().split())))
    
    dp[0][1] += dp[1][0]
    dp[1][1] += dp[0][0]
    
    for i in range(2, N):
        dp[0][i] += max(dp[1][i - 1], dp[1][i - 1])
        dp[1][i] += max(dp[0][i - 1], dp[0][i - 2])
        
    print(max(dp[0][N - 1], dp[1][N - 1]))

# Old Codes
dx1 = [0, 1, 1]
dy1 = [-2, -2, -1]
dx2 = [0, -1, -1]
dy2 = [-2, -2, -1]

T = int(input())
for _ in range(T):
    N = int(input())
    d = []
    d.append(list(map(int, input().split())))
    d.append(list(map(int, input().split())))
    
    dp = [[0 for _ in range(N)] for _ in range(2)]
    
    dp[0][0] = d[0][0]
    dp[1][0] = d[1][0]
    dp[0][1] = d[0][1] + d[1][0]
    dp[1][1] = d[1][1] + d[0][0]
    
    x, y = 0, 0
    for i in range(2, N):
        for j in range(3):
            nx1, ny1 = 0 + dx1[j], i + dy1[j]
            nx2, ny2 = 1 + dx2[j], i + dy2[j]
            dp[0][i] = max(dp[0][i], dp[nx1][ny1] + d[0][i])
            dp[1][i] = max(dp[1][i], dp[nx2][ny2] + d[1][i])
        
    print(max(dp[0][N - 1], dp[1][N - 1]))
        