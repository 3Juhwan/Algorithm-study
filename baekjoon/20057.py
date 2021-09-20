import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def sweep(x, y, d):
    global answer

    arr = list(map(lambda a: int(graph[x][y] * a), [0.01, 0.02, 0.05, 0.07, 0.1]))
    l_arr = [arr[0], arr[0], arr[1], arr[1], arr[2], arr[3], arr[3], arr[4], arr[4]]
    l_arr.append(graph[x][y] - sum(l_arr))
    graph[x][y] = 0

    if d == 0:
        dxy = [(1, -1), (1, 1), (0, -2), (0, 2), (-2, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (-1, 0)]
        for i in range(10):
            nx, ny = x + dxy[i][0], y + dxy[i][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                answer += l_arr[i]
            else:
                graph[nx][ny] += l_arr[i]

    elif d == 1:
        dxy = [(-1, 1), (1, 1), (-2, 0), (2, 0), (0, -2), (-1, 0), (1, 0), (-1, -1), (1, -1), (0, -1)]
        for i in range(10):
            nx, ny = x + dxy[i][0], y + dxy[i][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                answer += l_arr[i]
            else:
                graph[nx][ny] += l_arr[i]

    elif d == 2:
        dxy = [(-1, -1), (-1, 1), (0, -2), (0, 2), (2, 0), (0, -1), (0, 1), (1, -1), (1, 1), (1, 0)]
        for i in range(10):
            nx, ny = x + dxy[i][0], y + dxy[i][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                answer += l_arr[i]
            else:
                graph[nx][ny] += l_arr[i]

    elif d == 3:
        dxy = [(-1, -1), (1, -1), (-2, 0), (2, 0), (0, 2), (-1, 0), (1, 0), (-1, 1), (1, 1), (0, 1)]
        for i in range(10):
            nx, ny = x + dxy[i][0], y + dxy[i][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                answer += l_arr[i]
            else:
                graph[nx][ny] += l_arr[i]


n = int(input())
graph = [list(map(int, input().split())) for __ in range(n)]

visited = [[0] * n for __ in range(n)]
x, y = [n//2] * 2
d = 1

answer = 0

while x or y:
    visited[x][y] = 1
    x, y = x + dx[d], y + dy[d]
    sweep(x, y, d)

    dd = (d + 1) % 4
    tx, ty = x + dx[dd], y + dy[dd]
    if not visited[tx][ty]:
        d = dd

print(answer)