import sys
input = sys.stdin.readline

def dfs(x):
    global result
    visited[x] = 1
    cycle.append(x)
    num = graph[x]
    
    if visited[num]:
        if num in cycle:
            result += cycle[cycle.index(num):]
        return
    else:
        dfs(num)

t = int(input())
for _ in range(t):
    n = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [0] * (n + 1)
    result = []
    
    for i in range(1, n + 1):
        if not visited[i]:
            cycle = []
            dfs(i)
    
    print(n - len(result))