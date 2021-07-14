n = int(input())
m = int(input())
vip = [0] * (n + 1)
for _ in range(m): vip[int(input())] = 1
dp = [1] * (n + 1)
result = 1
for i in range(2, n + 1):
    if vip[i] == 1:
        result *= dp[i-1]
    else:
        dp[i] = dp[i-1] + dp[i-2] if not vip[i-1] else 1

result *= dp[-1]
print(result)