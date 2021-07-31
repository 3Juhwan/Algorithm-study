import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y, visited):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == graph[x][y]:
            visited[nx][ny] = 1
            dfs(nx, ny, visited)

def getSection():
    result = 0
    visited = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = 1
                dfs(i, j, visited)
                result += 1

    return result

# INPUT
n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]

# RUN
print(getSection(), end=' ')

# Convert R to G
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

# RUN
print(getSection())