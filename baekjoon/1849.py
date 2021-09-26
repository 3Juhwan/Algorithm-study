from math import ceil, log2
import sys
input = sys.stdin.readline
NUM = 100_000


def init(start, end, node):
    if start == end:
        tree[node] = 1
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init(start, mid, node*2) + init(mid+1, end, node*2+1)
    return tree[node]


def update(start, end, node, target, dif):
    tree[node] += dif
    if start == end:
        return start
    mid = (start + end) // 2
    if tree[node*2] >= target:
        return update(start, mid, node*2, target, dif)
    else:
        return update(mid+1, end, node*2+1, target-tree[node*2], dif)


n = int(input())
arr = [int(input()) for __ in range(n)]

h = int(ceil(log2(NUM)))
t_size = 1 << (h+1)
tree = [0] * t_size
init(0, n-1, 1)

answer = [0] * n
for i in range(n):
    num = update(0, n-1, 1, arr[i]+1, -1)
    answer[num] = i + 1

for d in answer:
    print(d)