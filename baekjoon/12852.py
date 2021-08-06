from collections import deque

n = int(input())
dp = [[i] for i in range(n+1)]

q = deque([n])
while q:
    x = q.popleft()
    
    if x == 1:
        break
    # x // 3
    num = x // 3
    if x % 3 == 0 and (len(dp[num]) == 1 or len(dp[num]) > len(dp[x]) + 1):
        dp[num] = dp[x] + [num]
        q.append(num)
    # x // 2
    num = x // 2
    if x % 2 == 0 and (len(dp[num]) == 1 or len(dp[num]) > len(dp[x]) + 1):
        dp[num] = dp[x] + [num]
        q.append(num)
    # x - 1
    num = x - 1
    if x > 0 and (len(dp[num]) == 1 or len(dp[num]) > len(dp[x]) + 1):
        dp[num] = dp[x] + [num]
        q.append(num)

print(len(dp[1]) - 1)
print(*dp[1])