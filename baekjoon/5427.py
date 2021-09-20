import sys
input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def fireMove(fires):
    n, m = len(graph), len(graph[0])
    nfires = []
    for x, y in fires:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '.':
                nfires.append((nx, ny))
                graph[nx][ny] = '*'

    return nfires


def manMove(men):
    global answer, visited
    n, m = len(graph), len(graph[0])
    nmen = []
    for now, x, y in men:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                answer = min(answer, now+1)
            elif visited[nx][ny]:
                continue
            elif graph[nx][ny] == '.':
                nmen.append((now+1, nx, ny))
                visited[nx][ny] = 1

    return nmen


t = int(input())

for __ in range(t):
    m, n = map(int, input().split())
    graph = [list(input().rstrip()) for __ in range(n)]

    men, fires = [], []
    answer = INF
    visited = [[0] * m for __ in range(n)]

    for i in range(n):
        for j in range(m):
            if graph[i][j] == '@':
                men.append((0, i, j))
                graph[i][j] = '.'

    for i in range(n):
        for j in range(m):
            if graph[i][j] == '*':
                fires.append((i, j))

    while men:
        fires = fireMove(fires)
        men = manMove(men)

        if not answer == INF:
            break

	print(answer if answer < INF else 'IMPOSSIBLE')