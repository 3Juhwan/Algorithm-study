import heapq
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(M):
    graph.append(list(input().rstrip()))

dp = [[0] * N for _ in range(M)]
dp[0][0] = 0
visited = [[0] * N for _ in range(M)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    
    while q:
        now, xy = heapq.heappop(q)
        x, y = xy
        visited[x][y] = 1
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N or visited[nx][ny]:
                continue
            if graph[nx][ny] == '0':
                dp[nx][ny] = now
            else:
                dp[nx][ny] = dp[x][y] + 1
                
            if not visited[nx][ny]:
                heapq.heappush(q, (dp[nx][ny], (nx, ny)))
                visited[nx][ny] = 1
            
dijkstra((0, 0))

print(dp[M - 1][N - 1])