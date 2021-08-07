import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n = int(input())
m = int(input())
edges = [list(map(int, input().split())) for _ in range(m)]
result = 0

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

edges.sort(key=lambda x: x[2])

for edge in edges:
    a, b, cost = edge
    
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)