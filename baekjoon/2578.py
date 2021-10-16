graph = [list(map(int, input().split())) for __ in range(5)]
visited = [[0]*5 for __ in range(5)]

numbers = []
for __ in range(5):
    numbers += list(map(int, input().split()))

for idx, num in enumerate(numbers):
    for i in range(5):
        for j in range(5):
            if graph[i][j] == num:
                visited[i][j] = 1

    cnt = 0
    for i in range(5):
        t_cnt = 0
        for j in range(5):
            if visited[i][j]:
                t_cnt += 1
        if t_cnt == 5:
            cnt += 1

    for i in range(5):
        t_cnt = 0
        for j in range(5):
            if visited[j][i]:
                t_cnt += 1
        if t_cnt == 5:
            cnt += 1

    t_cnt = 0
    for i in range(5):
        if visited[i][i]:
            t_cnt += 1
    if t_cnt == 5:
        cnt += 1

    t_cnt = 0
    for i in range(5):
        if visited[i][4-i]:
            t_cnt += 1
    if t_cnt == 5:
        cnt += 1
    if cnt >= 3:
        print(idx+1)
        break