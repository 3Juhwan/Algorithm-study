import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
sex = [''] + list(input().rstrip().split())
edges = [list(map(int, input().split())) for __ in range(m)]

edges.sort(key=lambda x: x[2])

parent = list(range(n + 1))
visited = [0] * (n + 1)

result = 0

for edge in edges:
    a, b, cost = edge
    
    if sex[a] == sex[b]:
        continue
    
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        visited[a], visited[b] = [1] * 2
        result += cost
        
print(result)
print(-1 if 0 in visited[1:] else result)