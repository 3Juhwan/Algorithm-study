import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if generator[a]:
        parent[b] = a
        return
    elif generator[b]:
        parent[a] = b
        return
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m, k = map(int, input().split())
generator = [0] * (n + 1)
for x in map(int, input().split()):
    generator[x] = 1
edges = [list(map(int, input().split())) for __ in range(m)]

edges.sort(key=lambda x: x[2])

parent = list(range(n + 1))

result = 0
for edge in edges:
    a, b, cost = edge
    parent_a, parent_b = find_parent(parent, a), find_parent(parent, b)
    
    if generator[parent_a] and generator[parent_b]:
        continue
    
    if parent_a != parent_b:
        union_parent(parent, a, b)
        result += cost
    
print(result)