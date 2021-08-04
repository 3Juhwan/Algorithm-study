import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def spreadFineDust(graph):
    spreadGraph = [[0] * c for _ in range(r)]    # 각 칸에 확산된 미세먼지 양을 저장
    
    for x in range(r):
        for y in range(c):
            if graph[x][y] >= 5:
                spreadAmount, spreadCnt = graph[x][y] // 5, 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < r and 0 <= ny < c and not graph[nx][ny] == -1:
                        spreadGraph[nx][ny] += spreadAmount
                        spreadCnt += 1
                
                # 확산양 빼기
                graph[x][y] -= spreadAmount * spreadCnt
    
    for i in range(r):
        for j in range(c):
            graph[i][j] += spreadGraph[i][j]

def circulateAirClockWise(x):
    for i in range(x + 1, r - 1):
        graph[i][0] = graph[i + 1][0]
    for i in range(0, c - 1):
        graph[r - 1][i] = graph[r - 1][i + 1]
    for i in range(r - 1, x, -1):
        graph[i][c - 1] = graph[i - 1][c - 1]
    for i in range(c - 1, 1, -1):
        graph[x][i] = graph[x][i - 1]
    graph[x][1] = 0
    
def circulateCounterAirClockWise(x):
    for i in range(x - 1, 0, -1):
        graph[i][0] = graph[i - 1][0]
    for i in range(0, c - 1):
        graph[0][i] = graph[0][i + 1]
    for i in range(0, x):
        graph[i][c - 1] = graph[i + 1][c - 1]
    for i in range(c - 1, 1, -1):
        graph[x][i] = graph[x][i - 1]
    graph[x][1] = 0

# 입력
r, c, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]

# 공기청정기 위치
airCleaner = [(i, 0) for i in range(r) if graph[i][0] == -1]

# 실행
for _ in range(t):
    # 미세먼지 확산
    spreadFineDust(graph)
    
    # 공기청정기 순환
    circulateCounterAirClockWise(airCleaner[0][0])
    circulateAirClockWise(airCleaner[1][0])
    
print(sum([x for row in graph for x in row]) + 2)