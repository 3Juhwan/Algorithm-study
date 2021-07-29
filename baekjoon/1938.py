from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def canMove(x, y, direction):
    if direction: # 세로 방향
        pos = [(x + i, y) for i in range(-1, 2, 1)]
    else: # 가로 방향
        pos = [(x, y + i) for i in range(-1, 2, 1)]
    
    for x, y in pos:
        if x < 0 or x >= n or y < 0 or y >= n:
            return 0
        if graph[x][y] == '1':
            return 0
    return 1

def canTurn(x, y):
    pos = [(x + i, y + j) for i in range(-1, 2, 1) for j in range(-1, 2, 1)]
    for x, y in pos:
        if x < 0 or x >= n or y < 0 or y >= n or graph[x][y] == '1':
            return 0
    return 1
    
# 입력
n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
dp = [[[0] * 2 for _ in range(n)] for _ in range(n)]

# 통나무 위치
log = [(i, j) for i in range(n) for j in range(n) if graph[i][j] == 'B']

# 목표 위치
target = [(i, j) for i in range(n) for j in range(n) if graph[i][j] == 'E']

# 방향 (1: 세로, 2: 가로)
direction = 1 if log[0][0] - log[1][0] else 0

# 중심점과 방향
logInfo = (log[1][0], log[1][1], direction)

# 목표 방향 (1: 세로, 2: 가로)
targetDirection = 1 if target[0][0] - target[1][0] else 0

# 목표 중심점과 방향
targetInfo = (target[1][0], target[1][1], targetDirection)

# BFS
q = deque([logInfo])

while q:
    x, y, direction = q.popleft()
    
    # UP DOWN LEFT RIGHT
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if canMove(nx, ny, direction) and not dp[nx][ny][direction]:
            q.append((nx, ny, direction))
            dp[nx][ny][direction] = dp[x][y][direction] + 1
    
    # TURN
    if canTurn(x, y) and not dp[x][y][not direction]:
        q.append((x, y, not direction))
        dp[x][y][not direction] = dp[x][y][direction] + 1

# OUTPUT
x, y, direction = targetInfo
print(dp[x][y][direction])