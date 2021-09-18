import heapq
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr, bag = [], []
for _ in range(N):
    arr.append(list(map(int, input().split())))
for _ in range(K):
    bag.append(int(input()))
arr.sort()
bag.sort()

q = []
i, result = 0, 0
for x in bag:
    while i < N and arr[i][0] <= x:
        heapq.heappush(q, -arr[i][1])
        i += 1
    if q: result -= heapq.heappop(q)
print(result)