from copy import deepcopy
import sys
input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]


def fish_mov(graph, fish_loc):
    for i in range(1, 17):
        x, y = fish_loc[i]
        if x == -1 and y == -1:
            continue

        num, dir = graph[x][y]
        for d in range(dir, dir + 8):
            d = d % 8
            nx, ny = x + dx[d], y + dy[d]

            # 범위 밖, 상어
            if nx < 1 or nx > 4 or ny < 1 or ny > 4 or graph[nx][ny][0] == -1:
                continue

            n_num, n_dir = graph[nx][ny]
            graph[x][y], graph[nx][ny] = (n_num, n_dir), (num, d)

            # 빈칸
            if n_num == 0:
                fish_loc[num] = (nx, ny)

            # 다른 물고기
            else:
                fish_loc[num], fish_loc[n_num] = (nx, ny), (x, y)
            break


def shark_mov(graph, shark_loc, fish_loc):
    t_graph = deepcopy(graph)
    t_fish_loc = deepcopy(fish_loc)

    x, y = shark_loc
    num, dir = t_graph[x][y]
    t_fish_loc[num] = (-1, -1)
    t_graph[x][y] = (-1, dir)     # 현재 위치에 상어 저장

    nx, ny = x + dx[dir], y + dy[dir]
    # 범위 벗어나면 return 0
    if nx < 1 or nx > 4 or ny < 1 or ny > 4:
        return num

    # 물고기 이동
    fish_mov(t_graph, t_fish_loc)

    t_graph[x][y] = (0, 0)
    answer = 0
    # 물고기 잡아 먹기
    while 1 <= nx <= 4 and 1 <= ny <= 4:
        if not t_graph[nx][ny][0] == 0:
            tmp = shark_mov(t_graph, (nx, ny), t_fish_loc)
            answer = max(answer, tmp)
        nx, ny = nx + dx[dir], ny + dy[dir]
    return answer + num    # 다음에서 max + 현재 물고기


# 벽&빈칸이면 -1, 상어면 0, 물고기 a
graph = [[(None)] * 5 for __ in range(5)]
fish_loc = [(0, 0)] * 17

for i in range(1, 5):
    line = list(map(int, input().split()))
    for j in range(4):
        graph[i][j+1] = (line[2*j], line[2*j+1]-1)
        fish_loc[line[2*j]] = (i, j+1)

print(shark_mov(graph, (1, 1), fish_loc))