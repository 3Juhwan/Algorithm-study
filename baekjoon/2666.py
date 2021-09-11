from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e5)

n = int(input())
door1, door2 = map(int, input().split())
t = int(input())
arr = [int(input()) for __ in range(t)]

dp = [[[INF] * 21 for __ in range(21)] for __ in range(21)]
dp[0] = [[0] * 21 for __ in range(21)]

q = deque([(0, door1, door2)])    # index, door1, door2
while q:
    idx, door1, door2 = q.popleft()
    if idx == t:
        continue
    
    now = arr[idx]
    
    dp[idx+1][now][door2] = min(dp[idx+1][now][door2], abs(now - door1) + dp[idx][door1][door2])
    dp[idx+1][door1][now] = min(dp[idx+1][door1][now], abs(now - door2) + dp[idx][door1][door2])
    
    q.append((idx+1, now, door2))
    q.append((idx+1, door1, now))

print(min(map(min, dp[t])))