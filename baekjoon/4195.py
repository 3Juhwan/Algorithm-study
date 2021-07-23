import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]
    
def union(parent, num, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
        num[a] += num[b]
    elif a > b:
        parent[a] = b
        num[b] += num[a]

t = int(input())
for _ in range(t):
    n = int(input())
    names = {}
    parent = [0] + list(range(1, 200_001))
    num = [1] * (200_001)
    for _ in range(n):
        a, b = input().rstrip().split()
        if a not in names: names[a] = len(names) + 1
        if b not in names: names[b] = len(names) + 1
        
        union(parent, num, names[a], names[b])
        print(num[find(names[a])])