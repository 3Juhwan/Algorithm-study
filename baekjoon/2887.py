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
planets = [[i] + list(map(int, input().split())) for i in range(1, n + 1)]
parent = list(range(n + 1))
result = 0

edges = []

for i in range(1, 4):
    planets.sort(key=lambda x: x[i])
    for j in range(1, n):
        cost = abs(planets[j-1][i] - planets[j][i])
        edges.append((cost, planets[j-1][0], planets[j][0]))

edges.sort()

for edge in edges:
    cost, a, b = edge
    
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)