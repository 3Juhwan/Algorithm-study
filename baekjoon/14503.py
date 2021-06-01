import sys
input = sys.stdin.readline

# input
N, M = map(int, input().split())
r, c, d = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# 북동남서 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y = r, c
result, cnt = 0, 0

while True:
    # 1
    if graph[x][y] == 0:
        result += 1
        graph[x][y] = 2

    # setting
    i = (d + 3) % 4
    nx, ny = x + dx[i], y + dy[i]
    
    backIdx = (d + 2) % 4
    bnx, bny = x + dx[backIdx], y + dy[backIdx]

    # 2-a
    if not graph[nx][ny]:
        x, y, d = nx, ny, i
        cnt = 0
    # 2-b
    elif cnt < 4:
        d = i
        cnt += 1
    # 2-d
    elif graph[bnx][bny] == 1:
        break
    # 2-c
    else:
        x, y = bnx, bny
        cnt = 0

print(result)