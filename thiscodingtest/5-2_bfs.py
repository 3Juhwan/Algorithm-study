from collections import deque

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

# 상하좌우
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y):
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()
        value = graph[x][y]

        # 출구에 도착한 경우
        if x == N - 1 and y == M - 1:
            return value

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 범위를 벗어난 경우
            if nx <= -1 or nx >= N or ny <= -1 or ny >= M:
                continue

            # 해당 노드를 처음 방문하는 경우에 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = value + 1
                queue.append((nx, ny))

result = bfs(0, 0)
print(result)