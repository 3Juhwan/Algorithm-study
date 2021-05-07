dp = [1 for _ in range(10)]

N = int(input())

for _ in range(1, N):
    for i in range(0, 10):
        dp[i] = sum(dp[i:])
    
print('result =', sum(dp))