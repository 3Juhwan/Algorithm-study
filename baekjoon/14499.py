import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
command = list(map(int, input().split()))

def moveDice(dice, x):
    # 1: 동 | 2: 서 | 3: 북 | 4: 남
    if x == 1:
        dice[1], dice[0], dice[5], dice[3], dice[2] = dice[1], dice[2], dice[3], dice[0], dice[5]
    elif x == 2:
        dice[1], dice[0], dice[5], dice[3], dice[2] = dice[1], dice[3], dice[2], dice[5], dice[0]
    elif x == 3:
        dice[1], dice[0], dice[4], dice[5] = dice[5], dice[1], dice[0], dice[4]
    elif x == 4:
        dice[1], dice[0], dice[4], dice[5] = dice[0], dice[4], dice[5], dice[1]

dice = [0, 0, 0, 0, 0, 0]
nowX, nowY = x, y

for com in command:
    nx, ny = nowX + dx[com-1], nowY + dy[com-1]
    if 0 <= nx < n and 0 <= ny < m:
        nowX, nowY = nx, ny
        moveDice(dice, com)
        
        if graph[nowX][nowY] == 0:
            graph[nowX][nowY] = dice[0]
        else:
            dice[0] = graph[nowX][nowY]
            graph[nowX][nowY] = 0
            
        print(dice[5])