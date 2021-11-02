import sys
sys.setrecursionlimit(3000)
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, m = map(int, input().split())
graph = [input().rstrip() for __ in range(n)]

visited = [[0]*m for __ in range(n)]
dp = [[-1]*m for __ in range(n)]

flag = 0


def mvCoin(x, y):
    global flag
    if visited[x][y]:
        flag = 1
        return 0

    visited[x][y] = 1

    ret = dp[x][y]
    if ret != -1:
        visited[x][y] = 0
        return ret

    ret = 0
    for i in range(4):
        step = int(graph[x][y])
        nx, ny = x+dx[i]*step, y+dy[i]*step
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == 'H':
            continue
        ret = max(ret, mvCoin(nx, ny) + 1)

    visited[x][y] = 0

    dp[x][y] = ret
    return ret


answer = 1 + mvCoin(0, 0)
print(answer if not flag else -1)