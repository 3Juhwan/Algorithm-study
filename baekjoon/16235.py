from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

n, m, k = map(int, input().split())
food = [list(map(int, input().split())) for __ in range(n)]
woods = [[deque() for __ in range(n)] for __ in range(n)]
for __ in range(m):
    x, y, age = map(int, input().split())
    woods[x-1][y-1].append(age)

graph = [[5] * n for __ in range(n)]

for __ in range(k):
    # 봄 여름
    for i in range(n):
        for j in range(n):
            woods_num = len(woods[i][j])
            for k in range(woods_num):
                age = woods[i][j][k]

                if graph[i][j] >= age:
                    graph[i][j] -= age
                    woods[i][j][k] += 1
                else:
                    for _ in range(k, woods_num):
                        graph[i][j] += woods[i][j].pop() // 2
                    break
    
    # 가을 겨울
    for i in range(n):
        for j in range(n):
            for k in range(len(woods[i][j])):
                age = woods[i][j][k]
                if age % 5 == 0:
                    for u in range(8):
                        nx, ny = i + dx[u], j + dy[u]
                        if 0 <= nx < n and 0 <= ny < n:
                            woods[nx][ny].appendleft(1)

            graph[i][j] += food[i][j]

result = 0
for i in range(n):
    for j in range(n):
        result += len(woods[i][j])
print(result)