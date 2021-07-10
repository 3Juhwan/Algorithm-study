from itertools import combinations
import sys
input = sys.stdin.readline

# 여러 store과 현재 위치의 최소값 구하기
def getMinDist(now, store):
    x1, y1 = now
    minDist = 101
    for x2, y2 in store:
        dist = abs(x1-x2) + abs(y1-y2)
        minDist = min(minDist, dist)
    return minDist

# input
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 치킨집 위치 저장
store = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            store.append((i, j))

# 전체 치킨집에서 m개를 선택한 조합
setStore = list(combinations(store, m))

# Run
result = int(1e9)
for s in setStore:
    sumDist = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                sumDist += getMinDist((i, j), s)
    result = min(result, sumDist)

# Output
print(result)