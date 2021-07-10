from copy import deepcopy
from itertools import permutations
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
calculate = [list(map(int, input().split())) for _ in range(K)]

def getArraySum(array):
    return min(sum(x) for x in array)
    
def turn(graph, cal):
    r, c, s = cal
    lx, ly, rx, ry = r-s-1, c-s-1, r+s-1, c+s-1
    
    # 회전
    while lx < rx and ly < ry:
        t1, t2, t3 = graph[lx][ry], graph[rx][ry], graph[rx][ly]
        for y in range(ry, ly, -1):
            graph[lx][y] = graph[lx][y-1]
        for x in range(rx, lx, -1):
            graph[x][ry] = graph[x-1][ry]
        graph[lx+1][ry] = t1
        for y in range(ly, ry):
            graph[rx][y] = graph[rx][y+1]
        graph[rx][ry-1] = t2
        for x in range(lx, rx):
            graph[x][ly] = graph[x+1][ly]
        graph[rx-1][ly] = t3
        lx, ly, rx, ry = lx+1, ly+1, rx-1, ry-1

result = int(1e9)
for x in list(permutations(calculate, K)):
    g = deepcopy(graph)
    for a in x: turn(g, a)
    result = min(result, getArraySum(g))
print(result)