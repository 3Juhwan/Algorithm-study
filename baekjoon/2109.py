import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = [tuple(map(int, input().split())) for __ in range(n)]
arr.sort(key=lambda x: (x[1], -x[0]))

q, limit = [], 0
for x in arr:
    limit = x[1]
    if len(q) < limit:
        heapq.heappush(q, x)
    else:
        if q[0][0] < x[0]:
            heapq.heappop(q)
            heapq.heappush(q, x)

print(sum([x[0] for x in q]))