import sys
from math import *
input = sys.stdin.readline
MOV = 1_000_000_007


def init(start, end, node):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = (init(start, mid, node*2) * init(mid+1, end, node*2+1)) % MOV
    return tree[node]


def getMul(start, end, node, left, right):
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return (getMul(start, mid, node*2, left, right) * getMul(mid+1, end, node*2+1, left, right)) % MOV


def update(start, end, node, index, dif):
    if index < start or index > end:
        return -1
    if start == end:
        tree[node] = dif
        return -1
    mid = (start + end) // 2
    update(start, mid, node * 2, index, dif)
    update(mid + 1, end, node * 2 + 1, index, dif)
    tree[node] = (tree[node*2] * tree[node*2+1]) % MOV


n, m, k = map(int, input().split())
arr = [int(input()) for __ in range(n)]

h = int(ceil(log2(n)))
t_size = 1 << (h+1)

tree = [0] * t_size
init(0, len(arr)-1, 1)

for __ in range(m+k):
    a, b, c = map(int, input().split())
    
    if a == 1:
        arr[b-1] = c
        update(0, len(arr)-1, 1, b-1, c)
    else:
        print(getMul(0, len(arr)-1, 1, b-1, c-1))