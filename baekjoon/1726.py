import heapq
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def convertDir(x):
    if x == 0: return 3
    elif x == 1: return 1
    elif x == 2: return 2
    else: return 0


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for __ in range(n)]
sx, sy, sd = map(lambda x: int(x)-1, input().split())
ex, ey, ed = map(lambda x: int(x)-1, input().split())
sd = convertDir(sd)
ed = convertDir(ed)
visited = [[[0] * m for __ in range(n)] for __ in range(4)]
visited[sd][sx][sy] = 1

answer = int(1e9)

q = [(0, sx, sy, sd)]
while q:
    cnt, x, y, d = heapq.heappop(q)
    if x == ex and y == ey and d == ed:
        answer = min(answer, cnt)
        break

    # 방향 전환
    for i in [-1, 1]:
        nd = (d + i + 4) % 4
        if not visited[nd][x][y]:
            visited[nd][x][y] = 1
            heapq.heappush(q, (cnt+1, x, y, nd))
    # 123 이동
    i = 1
    while i <= 3:
        nx, ny = x + dx[d] * i, y + dy[d] * i
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            if not visited[d][nx][ny]:
                visited[d][nx][ny] = 1
                heapq.heappush(q, (cnt+1, nx, ny, d))
            i += 1
        else:
            break

print(answer)