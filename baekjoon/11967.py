from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# input
N, M = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
switch = [[[] for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(M):
    x, y, a, b = map(int, input().split())
    switch[x][y].append((a, b))

# bfs에 방 불키는 로직만 추가
def bfs(x, y, result):
    queue = deque([(x, y)])
    visited = [[0] * (N + 1) for _ in range(N + 1)]
    
    visited[x][y] = 1
    graph[x][y] = 1
    update = 0    # 새로 갈 수 있게 된 방이 있다면, 1로 설정
    
    while queue:
        x, y = queue.popleft()

        # 새로 불킬 수 있는 방이 있는지 확인
        for a, b in switch[x][y]:
            if graph[a][b]:
                continue
                
            graph[a][b] = 1
            result += 1
            update = 1

        # 불 켜진 방으로 이동 (기본 bfs 로직)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx > N or ny < 0 or ny > N or visited[nx][ny] or not graph[nx][ny]:
                continue
                
            visited[nx][ny] = 1
            queue.append((nx, ny))

    return update, result

# Run
result, isContinue = 1, 1
while isContinue:
    isContinue, result = bfs(1, 1, result)
    
print(result)