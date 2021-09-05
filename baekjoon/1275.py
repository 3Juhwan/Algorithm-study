from math import *
import sys
input = sys.stdin.readline


def init(start, end, node):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init(start, mid, node*2) + init(mid+1, end, node*2+1)
    return tree[node]


def getSum(start, end, node, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return getSum(start, mid, node*2, left, right) + getSum(mid+1, end, node*2+1, left, right)


def update(start, end, node, idx, diff):
    if idx < start or idx > end:
        return -1
    tree[node] += diff
    if start == end:
        return -1
    mid = (start + end) // 2
    update(start, mid, node*2, idx, diff)
    update(mid+1, end, node*2+1, idx, diff)

n, q = map(int, input().split())
arr = list(map(int, input().split()))

h = int(ceil(log2(n)))
t_size = 1 << (h + 1)

tree = [0] * t_size
init(0, n-1, 1)
for __ in range(q):
    x, y, a, b = map(int, input().split())
    print(getSum(0, n-1, 1, x-1, y-1) if x < y else getSum(0, n-1, 1, y-1, x-1))
    diff = b - arr[a-1]
    arr[a-1] = b
    update(0, n-1, 1, a-1, diff)