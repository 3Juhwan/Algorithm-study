import sys
input = sys.stdin.readline


def init(start, end, node):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = min(init(start, mid, node*2), init(mid+1, end, node*2+1))
    return tree[node]


def getMin(start, end, node, left, right):
    if left > end or right < start:
        return int(1e9)
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return min(getMin(start, mid, node*2, left, right), getMin(mid+1, end, node*2+1, left, right))


n, m = map(int, input().split())
arr = [int(input()) for __ in range(n)]

tree = [0] * 1_000_000
init(0, len(arr)-1, 1)

for __ in range(m):
    a, b = map(int, input().split())
    print(getMin(0, len(arr)-1, 1, a-1, b-1))