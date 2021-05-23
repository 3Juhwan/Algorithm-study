import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

cnt = 1
N = int(input().rstrip())
while N:
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().rstrip().split())))

    distance = [[INF] * N for _ in range(N)]

    def dijkstra(x, y):
        q = []
        heapq.heappush(q, (graph[x][y], x, y))
        distance[0][0] = graph[0][0]

        while q:
            dist, x, y = heapq.heappop(q)
            if distance[x][y] < dist:
                continue

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue

                cost = dist + graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

    dijkstra(0, 0)
    print('Problem %d: %d' % (cnt, distance[N - 1][N - 1]))
    cnt += 1
    N = int(input().rstrip())