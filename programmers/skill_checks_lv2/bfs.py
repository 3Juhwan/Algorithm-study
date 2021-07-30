# 적 공격 문제
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y, maps):
    n, m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)]

    q = deque([(x, y)])
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if maps[nx][ny] == 1:
                    visited[nx][ny] = 1
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx, ny))

def solution(maps):    
    n, m = len(maps), len(maps[0])
    bfs(0, 0, maps)
    answer = maps[n - 1][m - 1] if maps[n - 1][m - 1] != 1 else -1
    
    return answer