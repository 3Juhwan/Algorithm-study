import sys
input = sys.stdin.readline

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]

# 상어 이동
def move(shark):
    x, y, s, d, z = shark
    cnt = s
    while cnt:
        x, y = x + dx[d], y + dy[d]
        if not 0 < x <= r or not 0 < y <= c:
            # 방향 전환
            if d == 1: d = 2
            elif d == 2: d = 1
            elif d == 3: d = 4
            elif d == 4: d = 3
            x, y = x + dx[d] * 2, y + dy[d] * 2
        cnt -= 1
    return (x, y, s, d, z)

# input
r, c, m = map(int, input().split())
sharks = [list(map(int, input().split())) for _ in range(m)]

# run
now, result = 0, 0
while now < c:
    aliveSharks = []
    sharks.sort()
        
    # 상어 그래프에 담기
    visited = [[0] * (c + 1) for _ in range(r + 1)]
    for shark in sharks:
        x, y, size1 = shark[0], shark[1], shark[4]
        if visited[x][y]:    # 해당 자리에 상어가 있다면, 
            size2 = aliveSharks[-1][4]
            # 그래프에 담길 정보는 leftover내의 위치
            if size1 > size2:
                aliveSharks.pop()
                aliveSharks.append(shark)
        else: aliveSharks.append(shark)
        visited[x][y] = len(aliveSharks)
            
    # 어부 이동
    now += 1
        
    # 상어 잡기
    for i in range(1, r + 1):
        if visited[i][now]:
            idx = visited[i][now] - 1
            result += aliveSharks[idx][4]
            del aliveSharks[idx]
            break
    
    # 상어 이동
    sharks = []
    for shark in aliveSharks:
        sharks.append(move(shark))

print(result)