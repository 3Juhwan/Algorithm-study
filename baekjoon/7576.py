from collections import deque
import sys

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

M, N = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

queue = deque([])
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))
    
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        
        if graph[nx][ny]:
            continue
        else:
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, ny))

result = 1
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            result = 0
            break
        result = max(result, graph[i][j])
    if not result:
        break
print(result - 1)