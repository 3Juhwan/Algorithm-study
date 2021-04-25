N, M = map(int, input().split())
x, y, r = map(int, input().split())
_map = []
for _ in range(N):
    _map.append(list(map(int, input().split())))
result = 0
    
# 초기 위치 방문
_map[x][y] = 2
result += 1

# 북서남동 순
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True:
    # 사방이 막혔을 때
    cnt = 0
    for i in range(4):
        mx, my = x + dx[i], y + dy[i]
        if _map[mx][my]:
            cnt += 1
    if cnt == 4:
        x, y = x - dx[r], y - dy[r] # 후진
        if _map[x][y] == 1:
            break
        continue
    
    # 갈 곳 있을 때
    r = (r + 3) % 4
    mx, my = x + dx[r], y + dy[r]
    
    if _map[mx][my] == 0:
        result += 1
        _map[mx][my] = 2
        x, y = mx, my
    
print(result)
