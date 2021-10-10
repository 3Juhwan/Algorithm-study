import sys
input = sys.stdin.readline

graph = [list(map(lambda x: 1 if x == 'O' else 0, input().rstrip())) for __ in range(10)]
answer = 101


def isTurnOff(graph):
	if sum([sum(x) for x in graph]): return False
	return True


def nextLocation(x, y):
    if y >= 10:
        return (x+1, 0)
    return (x, y)


def switch(graph, x, y):
	dx = [-1, 0, 0, 0, 1]
	dy = [0, -1, 0, 1, 0]

    for i in range(5):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < 10 and 0 <= ny < 10:
            graph[nx][ny] = 0 if graph[nx][ny] else 1


def dfs(graph, x, y, cnt):
    global answer
    if x >= 10:
        if isTurnOff(graph):
            answer = min(answer, cnt)
        return -1

    if x == 0:
        tx, ty = nextLocation(x, y+1)
        dfs(graph, tx, ty, cnt)
        switch(graph, x, y)

        tx, ty = nextLocation(x, y+1)
        dfs(graph, tx, ty, cnt+1)
        switch(graph, x, y)

    else:
        if graph[x-1][y]:
            switch(graph, x, y)
            tx, ty = nextLocation(x, y+1)
            dfs(graph, tx, ty, cnt+1)
            switch(graph, x, y)
        else:
            tx, ty = nextLocation(x, y+1)
            dfs(graph, tx, ty, cnt)


dfs(graph, 0, 0, 0)
print(answer if answer != 101 else -1)