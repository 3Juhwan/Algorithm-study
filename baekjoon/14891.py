from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1]

gear = [deque(list(map(int, input().rstrip()))) for _ in range(4)]
k = int(input())
command = [list(map(int, input().split())) for _ in range(k)]

def turnGear(gear, x):
    if x == 1: gear.appendleft(gear.pop())
    elif x == -1: gear.append(gear.popleft())
    return gear

def doRotate(gear1, gear2, x):
    if x == -1 and gear1[6] != gear2[2]:
        return 1
    if x == 1 and gear1[2] != gear2[6]:
        return 1
    return 0

for x in command:
    visited = [0] * 4
    visited[x[0]-1] = 1
    q = deque([(x[0]-1, x[-1])])    # 번호와 회전방향
    while q:
        now, turn = q.popleft()
        
        for i in range(2):
            nnow, nturn = now + dx[i], -turn
            if 0 <= nnow < 4 and not visited[nnow] and doRotate(gear[now], gear[nnow], dx[i]):
                q.append((nnow, nturn))
                visited[nnow] = 1
        
        # 회전
        gear[now] = turnGear(gear[now], turn)
        
        
result = 0
for i in range(4):
    result += gear[i][0] * pow(2, i)
print(result)