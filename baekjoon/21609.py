from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def rotate_a_matrix_by_90_degree(a):
    res = [[0] * n for __ in range(n)]

    for r in range(n):
        for c in range(n):
            res[n - 1 - c][r] = a[r][c]

    return res


def gravity(graph):
    for i in range(n):
        limit = n
        now = n-1

        while now >= 0:
            if graph[now][i] == -2:
                pass
            elif graph[now][i] == -1:
                limit = now
            else:
                graph[limit-1][i], graph[now][i] = graph[now][i], graph[limit-1][i]
                limit -= 1
            now -= 1


def findGroup(graph):
    visited = [[0] * n for __ in range(n)]
    s_rainbow, s_origin, s_std, r_blckgrp = 0, 0, 0, []

    for i in range(n):
        for j in range(n):			
            if not visited[i][j] and not graph[i][j] in [-2, -1, 0]:
                q = deque([(i, j)])
                t_visited = [[0] * n for __ in range(n)]
                visited[i][j], t_visited[i][j] = [1] * 2
                t_rainbow, t_origin, t_std, t_blckgrp = 0, 1, graph[i][j], [(i, j)]
                while q:
                    x, y = q.popleft()
                    for ii in range(4):
                        nx, ny = x + dx[ii], y + dy[ii]
                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue
                        if t_visited[nx][ny] or graph[nx][ny] in [-2, -1]:
                            continue
                        if graph[nx][ny] == 0:
                            t_rainbow += 1
                        else:
                            if not graph[nx][ny] == t_std:
                                continue
                            t_origin += 1
                            visited[nx][ny] = 1
                        t_visited[nx][ny] = 1
                        t_blckgrp.append((nx, ny))
                        q.append((nx, ny))

                if len(t_blckgrp) < 2:
                    continue
                if s_origin == 0:
                    s_rainbow, s_origin, s_std, r_blckgrp = t_rainbow, t_origin, t_std, t_blckgrp
                    continue

                t_all = (t_rainbow + t_origin, t_rainbow, t_blckgrp[0][0], t_blckgrp[0][1])
                s_all = (s_rainbow + s_origin, s_rainbow, r_blckgrp[0][0], r_blckgrp[0][1])				
                sort_by_std = sorted([t_all, s_all])
                if (sort_by_std[1][2], sort_by_std[1][3]) == r_blckgrp[0]:
                    continue
                else:
                    s_rainbow, s_origin, s_std, r_blckgrp = t_rainbow, t_origin, t_std, t_blckgrp

    return r_blckgrp		


def delBlock(graph, arr):
    for x, y in arr:
        graph[x][y] = -2


n, _ = map(int, input().split())
graph = [list(map(int, input().split())) for __ in range(n)]
answer = 0

while True:
    del_blck = findGroup(graph)
    if not del_blck:
        break
    answer += len(del_blck) * len(del_blck)

    delBlock(graph, del_blck)
    gravity(graph)
    graph = rotate_a_matrix_by_90_degree(graph)
    gravity(graph)

print(answer)