import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def getIndex(x):
    return ord(x) - ord('A')

def dfs(x, y, cnt):
    global result
    result = max(result, cnt)
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and not visited[getIndex(graph[nx][ny])]:
            visited[getIndex(graph[nx][ny])] = 1
            dfs(nx, ny, cnt + 1)

    cnt -= 1
    visited[getIndex(graph[x][y])] = 0

# INPUT
r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]

result = 0
visited = [0] * 26
visited[getIndex(graph[0][0])] = 1
dfs(0, 0, 1)
print(result)