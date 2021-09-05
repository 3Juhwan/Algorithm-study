from math import log2, ceil
import sys
input = sys.stdin.readline
MAX = 1000000

def update(start, end, node, idx, diff):
    if start > idx or end < idx:
        return -1
    tree[node] += diff
    if start == end:
        return 0
    mid = (start + end) // 2
    update(start, mid, node*2, idx, diff)
    update(mid+1, end, node*2+1, idx, diff)


def query(start, end, node, seq):
    if start == end:
        return start
    
    mid = (start + end) // 2
    if tree[node*2] >= seq:
        return query(start, mid, node*2, seq)
    else:
        return query(mid+1, end, node*2+1, seq - tree[node*2])


h = ceil(log2(MAX))
t_size = 1 << (h+1)
tree = [0] * t_size

n = int(input())
for __ in range(n):
    arr = list(map(int, input().split()))
    if arr[0] == 1:
        idx = query(0, MAX-1, 1, arr[1])
        print(idx)
        update(0, MAX-1, 1, idx, -1)
    else:
        update(0, MAX-1, 1, arr[1], arr[2])