from collections import deque
import heapq
import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 입력
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip().split())))


# 물고기가 있다면 위치와 거리가 반환되고, 없다면 (-1, -1, -1)이 반환된다
def eat_fish(position, size):
    x, y = position
    edible_fish = []

    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 0

    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        dist = visited[x][y]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny]:
                continue

            # 물고기가 상어보다 크다면
            if graph[nx][ny] > size:
                continue

            # 상어가 물고기보다 크거나 같으면
            elif graph[nx][ny] <= size:
                visited[nx][ny] = dist + 1
                q.append((nx, ny))

                # 상어가 물고기보다 크면 먹기
                if graph[nx][ny] > 0 and graph[nx][ny] < size:
                    heapq.heappush(edible_fish, (dist + 1, nx, ny))

    # 먹을 수 있는 물고기가 없으면
    if not edible_fish:
        return (-1, -1, -1)

    # 먹을 수 있는 물고기를 x와 y를 기준으로 정렬
    return heapq.heappop(edible_fish)

# 초기 변수 설정
shark_size = 2
result = 0
eaten_fish = 0

# 상어의 최초 위치 찾기
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            x, y = i, j

graph[x][y] = 0
while True:
    d, x, y = eat_fish((x, y), shark_size)
    if x == -1:
        break

    graph[x][y] = 0
    result += d
    eaten_fish += 1

    if eaten_fish == shark_size:
        eaten_fish = 0
        shark_size += 1

print(result)
