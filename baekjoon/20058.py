from copy import deepcopy
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def turnVector(graph, n, s):
	t_graph = deepcopy(graph)
	n = 1 << n
	size = 1 << s

    for i in range(0, n, size):
        for j in range(0, n, size):
            for x in range(size):
                tmp = [0] * size
                for y in range(size):
                    tmp[size-y-1] = graph[i+y][j+x]
                t_graph[i+x][j:j+size] = tmp

	return t_graph


def shrinkIce(graph, n):
    shrinkList = []
    n = 1 << n
    for i in range(n):
        for j in range(n):
            cnt = 0
            for x in range(4):
                nx, ny = i + dx[x], j + dy[x]
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny]:
                        cnt += 1

            if cnt <= 2 and graph[i][j]:
                shrinkList.append((i, j))

    for x, y in shrinkList:
        graph[x][y] -= 1


def getBiggestIce(graph):
    n = len(graph)
    answer = 0
    visited = [[0] * n for __ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j]:
                cnt = 0
                q = [(i, j)]
                while q:
                    x, y = q.pop()
                    for a in range(4):
                        nx, ny = x + dx[a], y + dy[a]
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny]:
                            visited[nx][ny] = 1
                            q.append((nx, ny))
                            cnt += 1
                answer = max(answer, cnt)
    return answer


n, q = map(int, input().split())
graph = [list(map(int, input().split())) for __ in range(1<<n)]

for command in map(int, input().split()):
	graph = turnVector(graph, n, command)
	shrinkIce(graph, n)

print(sum([sum(x) for x in graph]))
print(getBiggestIce(graph))