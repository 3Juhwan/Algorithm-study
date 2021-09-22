from copy import deepcopy
from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(visited, height, x, y):
    water = height - graph[x][y]
    q = deque([(x, y)])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if visited[nx][ny]:
                continue
            if nx in [0, n-1] or ny in [0, m-1]:
                if graph[nx][ny] < height:
                    return 0
                else:
                    visited[nx][ny] = 1
                    continue
            if graph[nx][ny] < height:
                water += height - graph[nx][ny]
                q.append((nx, ny))
            visited[nx][ny] = 1
    return water


n, m = map(int, input().split())
graph = [list(map(int, list(input().rstrip()))) for __ in range(n)]

answer = 0

visited = [[0] * m for __ in range(n)]
for h in range(9, 0, -1):
    for i in range(1, n-1):
        for j in range(1, m-1):
            if not visited[i][j] and graph[i][j] < h:
                t_visited = deepcopy(visited)
                rere = bfs(t_visited, h, i, j)
                if rere:
                    visited = t_visited
                    answer += rere

print(answer)