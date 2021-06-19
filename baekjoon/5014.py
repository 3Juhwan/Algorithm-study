import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
F, S, G, U, D = map(int, input().split())

floor = [INF] * (F + 1)
floor[S] = 0

q = []
heapq.heappush(q, (0, S))

while q:
    digit, now = heapq.heappop(q)
    upward, downward = now + U, now - D
    if upward <= F and floor[upward] > digit + 1:
        floor[upward] = digit + 1
        heapq.heappush(q, (digit + 1, upward))
    if downward > 0 and floor[downward] > digit + 1:
        floor[downward] = digit + 1
        heapq.heappush(q, (digit + 1, downward))
    
print(floor[G] if floor[G] < INF else "use the stairs")