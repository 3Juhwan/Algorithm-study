from itertools import combinations
from collections import deque
import sys

input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

sites, infect = [], []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0: sites.append((i, j))
        elif graph[i][j] == 2: infect.append((i, j))
            
full = len(sites) + len(infect) - 3
sites = list(combinations(sites, 3))

dfdf = 0
for site in sites:
    # 벽 세운 맵 만들기
    g = [a[:] for a in graph]
    for x, y in site: g[x][y] = 1

    result = len(infect)

    # 감염
    q = deque(infect)
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == 0:
                g[nx][ny] = 2
                q.append((nx, ny))
                result += 1
                
    dfdf = max(dfdf, full - result)

print(dfdf)