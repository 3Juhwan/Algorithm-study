from collections import deque
import sys
input = sys.stdin.readline

# UP LEFT RIGHT DOWN
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def isSeparated(x, y):
    q = deque([(x, y)])
    sepMinerals = []
    visited[x][y] = 1
    
    while q:
        x, y = q.popleft()
        sepMinerals.append((x, y))
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 'x':
                if nx == n - 1:
                    return []
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    
    return sepMinerals

def mineralDrop(minerals):
    visited = [0] * 100
    dropHeight = int(1e9)
    
    for x, y in minerals:
        if visited[y]:
            continue
        visited[y] = 1
        before = x
        
        while x + 1 < n and graph[x + 1][y] == '.':
            x += 1
        dropHeight = min(dropHeight, x - before) if x - before else dropHeight
        
    for x, y in minerals:
        graph[x][y] = '.'
        graph[x+dropHeight][y] = 'x'
        
n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
s = int(input())
bars = list(map(int, input().split()))

for i, bar in enumerate(bars):
    # 부술 곳 찾기
    index = [j for j, x in enumerate(graph[n - bar]) if x == 'x']
    if not index:
        continue
    
    # 막대가 부순 미네랄 위치
    x, y = n - bar, index[0] if i % 2 == 0 else index[-1]
    
    # 미네랄 부수기
    graph[x][y] = '.'
    
    # 부순 미네랄 주변 탐색
    for j in range(4):
        visited = [[0] * m for _ in range(n)]
        nx, ny = x + dx[j], y + dy[j]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 'x' and not visited[nx][ny]:
            result = isSeparated(nx, ny)    # 분리된 미네랄 덩어리라면, 그 미네랄 리스트 반환
            if not result:
                continue
            else:
                mineralDrop(sorted(result, reverse=True))
    
for g in graph:
    print(''.join(g))