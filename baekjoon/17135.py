# 힘들어서 막 작성한 코드,,,
from itertools import combinations
from copy import deepcopy
import sys
input = sys.stdin.readline

def getNearEnemy(graph, now, reach):    # 적 좌표랑 궁수의 (x, y) 위치 정보
    x, y = now
    row, column = len(graph), len(graph[0])
    r = 1
    
    while r <= reach:
        for i in range(-r, r + 1):
            nx, ny = x - (r - abs(i)), y + i
            if 0 <= nx < row and 0 <= ny < column and graph[nx][ny]:
                return (nx, ny)
        r += 1
    
    return (-1, -1)

# input
n, m, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# setting
sites = list(combinations(list(range(m)), 3))

result = 0
for site in sites:
    cnt = set()
    arr = deepcopy(graph)
    x = n
    while x > 0:    # row는 궁수들의 행 좌표
        for y in site:
            a, b = getNearEnemy(arr, (x, y), d)
            if not a == -1:
                cnt.add((a, b))        # 적 중복 계산!!!!!!!!!!!
        for q in cnt:
            g, h = q
            if g < x:
                arr[g][h] = 0
        arr.pop()    # 적 한 칸 이동
        x -= 1    # 궁수 한 칸 땡기기
    result = max(result, len(cnt))
print(result)