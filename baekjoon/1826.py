import heapq
import sys
input = sys.stdin.readline

# input
N = int(input())
dp = []
for _ in range(N):
    dp.append(list(map(int, input().split())))
dp.sort()
L, fuel = map(int, input().split())
dp.append([L, 0])

# run
result = 0
q = []
for i in range(N + 1):
    while q and fuel < dp[i][0]:
        fuel += (-1) * heapq.heappop(q)
        result += 1

    if dp[i][0] <= fuel:
        heapq.heappush(q, -dp[i][1])

print(result if fuel >= L else -1)