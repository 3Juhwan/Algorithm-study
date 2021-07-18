from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

left = 0

visited = [[0] * m for _ in range(n)]
visited[0][0] = 1
graph[0][0] = 2

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            left += 1

q = deque([(0, 0)])
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 0:
            graph[nx][ny] = 2
            visited[nx][ny] = 1
            q.append((nx, ny))
            
time = 0
while left > 0:
    melt, hole = [], []
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 2:
                continue
            if graph[x][y] == 0:
                hole.append((x, y))
                continue
            
            cnt = 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if graph[nx][ny] == 2:
                    cnt += 1
            if cnt >= 2:
                melt.append((x, y))
            
    while melt:
        x, y = melt.pop()
        graph[x][y] = 2
        left -= 1
        
    while hole:
        x, y = hole.pop()
        if not graph[x][y] == 0:
            continue
        cnt = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if graph[nx][ny] == 2:
                cnt += 1
                
        if cnt:
            stack = [(x, y)]
            graph[x][y] = 2
            while stack:
                x, y = stack.pop()
                
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = 2
                        stack.append((nx, ny))
    
    time += 1
    
print(time)