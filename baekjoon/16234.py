from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def bfs(now, visited):
    x, y = now
    visited[x][y] = 1
    result = [(x, y)]
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    result.append((nx, ny))
    return result

cnt = 0
while True:
    visited = [[0] * n for _ in range(n)]
    unions = []
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                tmp = bfs((i, j), visited)
                if len(tmp) > 1: unions.append(tmp)
    
    if len(unions) == 0: break
    
    for union in unions:
        avg = sum([graph[x][y] for x, y in union]) // len(union)
        for x, y in union: graph[x][y] = avg

    cnt += 1

print(cnt)