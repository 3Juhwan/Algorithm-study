from collections import deque
import sys
input = sys.stdin.readline

'''크루스칼'''

# 특정 원소가 속한 집합을 찾기
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기 (간선 연결한다고 생각!)
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

''''''

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(visited, now, number):
    q = deque([now])
    visited[now[0]][now[1]] = 1
    graph[now[0]][now[1]] = number

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1
                graph[nx][ny] = number

def color_map():
    global island_num
    
    number = 1
    visited = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j]:
                bfs(visited, (i, j), number)
                number += 1
    
    island_num = number - 1

def makeBridge(now, way):
    x, y = now
    nx, ny = x + dx[way], y + dy[way]
    cnt = 0
    
    while True:
        if nx < 0 or nx >= n or ny < 0 or ny >= m:        # 범위 넘어갔을 때
            return None
        if graph[nx][ny] == graph[x][y]:
            return None
        if graph[nx][ny] and not graph[nx][ny] == graph[x][y]:    # 다른 섬을 만났을 때
            if cnt > 1:
                return (cnt, graph[x][y], graph[nx][ny])
            else:
                return None
        if graph[nx][ny] == graph[x][y]:    # 다른 섬을 만났을 때
            return None
        nx, ny = nx + dx[way], ny + dy[way]
        cnt += 1
    
    return None

def get_bridges():
    bridges = []
    for i in range(n):
        for j in range(m):
            if graph[i][j]:
                for a in range(4):
                    nx, ny = i + dx[a], j + dy[a]
                    if 0 <= nx < n and 0 <= ny < m and not graph[nx][ny]:
                        bridge = makeBridge((i, j), a)
                        if bridge:
                            bridges.append(bridge)
    
    return bridges
    
# input
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

island_num = 0

# numbering an Isle
color_map()

bridges = get_bridges()

bridges.sort()

'''크루스칼'''
parent = [0] * (island_num + 1)
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, island_num + 1):
    parent[i] = i

for bridge in bridges:
    cost, a, b = bridge
    # 사이클이 발생하지 않는 경우에만 집합에 포함(=연결한다.)
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost

for i in range(1, island_num + 1):
	find(parent, i)
SET = set(parent)
print(result if len(SET) == 2 else -1)