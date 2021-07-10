from collections import deque
import sys
input = sys.stdin.readline

# input
n = int(input())
graph = [[0] * (n + 1) for _ in range(n + 1)]
k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    graph[x][y] = 1
l = int(input())
turn = [list(input().split()) for _ in range(l)]
for i in range(l): 
    turn[i][0] = int(turn[i][0])

# 상좌하우: 0123
def turnAround(now, x):
    if x == 'L':
        return (now + 1) % 4
    if x == 'D':
        return (now + 3) % 4

# 이동 불가하면 return 0, 이동가능하면 return 다음 좌표
def move(now, dir):
    x, y = now
    if dir == 0:
        if 0 < x-1 <= n:
            return (x-1, y)
        return 0
    elif dir == 1:
        if 0 < y-1 <= n:
            return (x, y-1)
        return 0
    elif dir == 2:
        if 0 < x+1 <= n:
            return (x+1, y)
        return 0
    elif dir == 3:
        if 0 < y+1 <= n:
            return (x, y+1)
        return 0

# Run
time, way, cnt = 0, 3, 0

q = deque([(1, 1)])
while True:
    time += 1
    tmp = move(q[0], way)
    
    # 이동할 수 없으면, 종료
    if not tmp: break
    # 이동할 수 있으면, 
    elif tmp:
        # 자기 몸에 부딫히면, 종료
        if tmp in q:
            break
        # 머리를 한 칸 앞으로
        q.appendleft(tmp)
        x, y = tmp
        # 사과가 있다면, 사과 먹기 냠냠
        if graph[x][y]: graph[x][y] = 0
        # 사과가 없다면, 꼬리 자르기
        else: q.pop()

    # 방향 전환
    if cnt < l and turn[cnt][0] == time:
        way = turnAround(way, turn[cnt][1])
        cnt += 1

# output
print(time)