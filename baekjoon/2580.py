from collections import deque
import sys
input = sys.stdin.readline

graph = [list(map(int, input().split())) for __ in range(9)]
arr = deque([(x, y) for x in range(9) for y in range(9) if graph[x][y] == 0])


def dfs(idx):
    if idx == len(arr):
        for x in graph:
            print(*x)
        sys.exit()

    x, y = arr[idx]
    poss_set = deque(getPossibleSet(x, y))
    while poss_set:
        num = poss_set.popleft()
        graph[x][y] = num
        dfs(idx+1)
        graph[x][y] = 0


def getPossibleSet(x, y):
    visited = [0] * 10
    for i in range(9):
        tmp = graph[x][i]
        visited[tmp] = 1

    for i in range(9):
        tmp = graph[i][y]
        visited[tmp] = 1

    x, y = x//3*3, y//3*3
    for i in range(3):
        for j in range(3):
            tmp = graph[x+i][y+j]
            visited[tmp] = 1

    return [i for i in range(1, 10) if not visited[i]]

dfs(0)