from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]

def bfs(x, y, num):
    cnt = 1
    dp[x][y][0] = 1
    
    stack = []
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        stack.append((x, y))
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not dp[nx][ny][0] and graph[nx][ny] == '0':
                q.append((nx, ny))
                dp[nx][ny][0] = 1
                cnt += 1
    
    for x, y in stack:
        dp[x][y] = [cnt, num]

# 메모리 냠냠
num = 0
dp = [[[0] * 2 for _ in range(m)] for _ in range(n)]
result = [[0] * m for _ in range(n)]

# dp에 연결정보 저장
for i in range(n):
    for j in range(m):
        if graph[i][j] == '0' and not dp[i][j][0]:
            bfs(i, j, num)
            num += 1    

for i in range(n):
    for j in range(m):
        if graph[i][j] == '1':
            visited = []
            result[i][j] = 1
            
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '0' and dp[nx][ny][1] not in visited:
                    result[i][j] += dp[nx][ny][0]
                    visited.append(dp[nx][ny][1])
                
# for g in dp: print(g)
for r in result:
    for a in r:
        print(a % 10, end='')
    print()