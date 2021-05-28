from collections import deque
import heapq
import sys

# init
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# input
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip().split())))
visited = [[0] * N for _ in range(N)]

# color the map
def bfs_color(i, j, num):
    queue = deque([(i, j)])
    graph[i][j] = num
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny]:
                continue
            if graph[nx][ny] and graph[nx][ny] <= num:
                graph[nx][ny] = num
                visited[nx][ny] = 1
                queue.append((nx, ny))

# Run "color the map"
num = 1
for i in range(N):
    for j in range(N):
        if graph[i][j] and not visited[i][j]:
            bfs_color(i, j, num)
            num += 1

# build bridge
def bfs_bridge(i, j, num):
    result = int(1e9)
    visited = [[0] * N for _ in range(N)]
    
    queue = []
    heapq.heappush(queue, (0, i, j))
    visited[i][j] = 1

    while queue:
        now, x, y = heapq.heappop(queue)

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny]:
                continue

            if graph[nx][ny] == num:
                visited[nx][ny] = 1
                heapq.heappush(queue, (now, nx, ny))
                continue
            elif graph[nx][ny] == 0:
                visited[nx][ny] = now + 1
                heapq.heappush(queue, (now + 1, nx, ny))
            else:
                result = min(result, now)
    return result

    
# Run build bridge
result = int(1e9)
num = 1
for i in range(N):
    for j in range(N):
        if graph[i][j] == num:
            result = min(result, bfs_bridge(i, j, num))
            num += 1
print(result)