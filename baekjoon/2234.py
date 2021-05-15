import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

digit = [8, 4, 2, 1]

# input
M, N = map(int, input().split())
visited = [[0] * M for __ in range(N)]
graph = []
for __ in range(N):
    graph.append(list(map(int, input().split())))

# dfs
def dfs(x, y):
    visited[x][y] = 1
    node = graph[x][y]
    cnt = 1

    for i in range(4):
        num = node - digit[i]
        if num >= 0:
            node = num
            continue

        nx, ny = x + dx[i], y + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < M and not visited[nx][ny]:
            cnt += dfs(nx, ny)
    return cnt

# run
result = []
for x in range(N):
    for y in range(M):
        if visited[x][y]:
            continue
        result.append(dfs(x, y))

output = 0
for x in range(N):
    for y in range(M):
        num = 1
        while num < 9:
            if num & graph[x][y]:
                visited = [[0] * M for __ in range(N)]
                graph[x][y] -= num
                output = max(output, dfs(x, y))
                graph[x][y] += num
            num *= 2

print(len(result))
print(max(result))
print(output)