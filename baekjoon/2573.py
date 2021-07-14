import sys
from collections import deque

input = sys.stdin.readline

def melt(x, y):
    surIce = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        # 범위 넘어가면 건너뛰기
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        
        if graph[nx][ny] <= 0:
            surIce += 1

    return surIce
    
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
        
            # 범위 넘어가면 건너뛰기
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            if graph[nx][ny] and visited[nx][ny] != 1:
                queue.append((nx, ny))
                visited[nx][ny] = 1
                
    return 1

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ice = deque([])
for x in range(N):
    for y in range(M):
        if graph[x][y] != 0:
            ice.append([x, y, 0])

year = 0
while True:
    if not ice:
        print(0)
        break

    year += 1
    
    # 빙산 녹이기
    for i in ice:
        i[2] = melt(i[0], i[1])
    
    leftoverIce = deque([])
    
    while ice:
        x, y, n = ice.popleft()
        if graph[x][y] <= n:
            graph[x][y] = 0
        else:
            graph[x][y] -= n
            leftoverIce.append([x, y, 0])
    
    visited = [[0 for _ in range(M)] for _ in range(N)]
    
    # bfs 확인
    cnt = 0
    for i in leftoverIce:
        x, y = i[0], i[1]
        if visited[x][y] != 1:
            cnt += bfs(i[0], i[1])
                
    if cnt > 1:
        print(year)
        break

    ice = leftoverIce