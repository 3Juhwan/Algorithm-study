from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# input
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip().split())))

# init
shark_size = 2
result = 0
eaten_fish = 0

def find_shark(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 9:
                return (i, j)
# If there is any fish, Eat fish and return shark's new position, else return (-1, -1, -1)
def find_fish(position, size):
    visited = [[0] * N for _ in range(N)]
    edible_fish, fish_dist = [], int(1e9)
    x, y = position

    visited[x][y] = 1
    q = deque([(0, x, y)])
    while q:
        dist, x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny]:
                continue

            # Cannot
            if graph[nx][ny] > size:
                continue

            # Move
            elif graph[nx][ny] <= size:
                visited[nx][ny] = 1
                q.append((dist + 1, nx, ny))

                # Eat
                if graph[nx][ny] > 0 and graph[nx][ny] < size:
                    if fish_dist == dist + 1:
                        edible_fish.append((nx, ny, dist + 1))
                    elif fish_dist > dist + 1:
                        fish_dist = dist + 1
                        edible_fish = [(nx, ny, dist + 1)]

    if not edible_fish:
        return (-1, -1, -1)

    edible_fish.sort(reverse=True, key=lambda x: (x[0], x[1]))
    return edible_fish.pop()

x, y = find_shark(N)
graph[x][y] = 0

while x >= 0 and y >= 0:
    x, y, d = find_fish((x, y), shark_size)
    graph[x][y] = 0
    result += d
    eaten_fish += 1
    if eaten_fish == shark_size:
        eaten_fish = 0
        shark_size += 1

print(result + 1)
