import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = [sorted(list(map(int, input().split()))) for __ in range(n)]
d = int(input())
arr.sort(key=lambda x: x[1])

answer = 0

q = []

for x, y in arr:
    if abs(x - y) <= d:
        heapq.heappush(q, x)
    while q and q[0] < y - d:
        heapq.heappop(q)
    answer = max(answer, len(q))

print(answer)