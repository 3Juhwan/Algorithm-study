from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(x, y, cnt):
    answer = 0
    q = deque([(x, y)])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 'L':
                visited[nx][ny] = visited[x][y] + 1
                answer = max(answer, visited[nx][ny])
                q.append((nx, ny))

    return answer


n, m = map(int, input().split())
graph = [list(input().rstrip()) for __ in range(n)]

answer = 0
for i in range(n):
    for j in range(m):
        visited = [[0] * m for __ in range(n)]
        if graph[i][j] == 'L':
            visited[i][j] = 1
            answer = max(answer, bfs(i, j, 0)-1)

print(answer)