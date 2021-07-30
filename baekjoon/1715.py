import heapq
import sys
input = sys.stdin.readline

q = []
result = 0

n = int(input())
for _ in range(n):
    heapq.heappush(q, int(input()))
    
while len(q) > 1:
    a, b = heapq.heappop(q), heapq.heappop(q)
    result += a + b
    heapq.heappush(q, a + b)

print(result)