import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

way = {
    'U': (-1, 0),
    'L': (0, -1),
    'D': (1, 0),
    'R': (0, 1)
}
    
def dfs(x, y):
    global result, cnt
    dx, dy = way[graph[x][y]]
    nx, ny = x + dx, y + dy
    
    if not visited[nx][ny]:
        visited[nx][ny] = cnt
        dfs(nx, ny)
    elif visited[nx][ny] == cnt:
        result += 1
    
n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
result, cnt = 0, 1

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            visited[i][j] = cnt
            dfs(i, j)
            cnt += 1
            
print(result)