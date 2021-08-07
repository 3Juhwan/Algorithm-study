from math import pow, sqrt
from itertools import combinations
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

def getDistance(s1, s2):
    x1, y1 = s1
    x2, y2 = s2
    
    return sqrt(pow(x1-x2) + pow(y1-y2))
    
n = int(input())
planets = [[i] + list(map(float, input().split())) for i in range(1, n + 1)]
parent = list(range(n + 1))
result = 0

edges = []

for a, b in combinations(planets, 2):
    cost = getDistance(a[1:], b[1:])
    edges.append((cost, a[0], b[0]))

edges.sort()

for edge in edges:
    cost, a, b = edge
    
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)