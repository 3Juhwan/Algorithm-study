import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

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

N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
tree = [0] * 30000000
init(0, N - 1, 1)
for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        b = b - 1
        diff = c - arr[b]
        arr[b] = c
        update(0, N - 1, 1, b, diff)
    elif a == 2:
        print(getSum(0, N - 1, 1, b - 1, c - 1))