from math import ceil, log2
import sys
input = sys.stdin.readline


'''Prefix Sum with Segment Tree'''
def init(start, end, node):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1)
    return tree[node]


def getSum(start, end, node, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return getSum(start, mid, node * 2, left, right) + getSum(mid + 1, end, node * 2 + 1, left, right)


def update(start, end, node, index, dif):
    if index < start or index > end:
        return -1
    tree[node] += dif
    if start == end:
        return -1
    mid = (start + end) // 2
    update(start, mid, node * 2, index, dif)
    update(mid + 1, end, node * 2 + 1, index, dif)


n = int(input())
p = [int(input()) for __ in range(n)]

idx = [0] * (n+1)
for i, x in enumerate(p, start=1):
    idx[x] = i

h = int(ceil(log2(n)))
t_size = 1 << (h+1)
tree = [0] * t_size
arr = [1] * n

init(0, n-1, 1)

i, j = 1, n
while i <= j:
    now = getSum(0, n-1, 1, 0, idx[i]-2)
    update(0, n-1, 1, idx[i]-1, -1)
    print(now)
    i += 1
    
    if i > j: break
    
    now = getSum(0, n-1, 1, idx[j], n-1)
    update(0, n-1, 1, idx[j]-1, -1)
    print(now)
    j -= 1