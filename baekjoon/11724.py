import sys
sys.setrecursionlimit(500_000_000)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visit = [0 for _ in range(N + 1)]
result = 0
# dfs
def dfs(v):
    visit[v] = 1
    for i in graph[v]:
        if visit[i]:
            continue
        dfs(i)

for i in range(1, N + 1):
    if visit[i]:
        continue
    dfs(i)
    result += 1

print(result)