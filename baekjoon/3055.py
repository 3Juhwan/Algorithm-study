from collections import deque
import sys
input = sys.stdin.readline

# init
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

bumped = ['D', 'S', 'X', '*']

# input
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input().rstrip()))

for i in range(N):
    for j in range(M):
        if graph[i][j].isdigit():
            graph[i][j] = int(graph[i][j])

# water move first
def bfs_waterflow():
    for i in range(N):
        for j in range(M):
            if not graph[i][j] == '*':
                continue

            queue = deque([(0, i, j)])

            visited = [[0] * M for _ in range(N)]
            visited[i][j] = 1

            while queue:
                now, x, y = queue.popleft()

                for n in range(4):
                    nx, ny = x + dx[n], y + dy[n]

                    if nx < 0 or nx >= N or ny < 0 or ny >= M:
                        continue
                    if graph[nx][ny] in bumped or visited[nx][ny]:
                        continue

                    graph[nx][ny] = now + 1

                    visited[nx][ny] = 1
                    queue.append((now + 1, nx, ny))

# find mole starting point
def start_point():
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 'S':
                start = (1, i, j)
                return start

# mole move next
def bfs_move(start):
    visited = [[0] * M for _ in range(N)]
    visited[start[1]][start[2]] = 1

    queue = deque([start])
    while queue:
        now, x, y = queue.popleft()

        for n in range(4):
            nx, ny = x + dx[n], y + dy[n]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 'D':
                return now
            if graph[nx][ny] in bumped or visited[nx][ny]:
                continue

            if graph[nx][ny] == '.' or graph[nx][ny] > now:
                visited[nx][ny] = 1
                queue.append((now + 1, nx, ny))
    return 0

# run
bfs_waterflow()
start = start_point()
result = bfs_move(start)

print(result if result else "KAKTUS")