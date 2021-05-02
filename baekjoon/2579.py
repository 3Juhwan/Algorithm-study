N = int(input())
arr = [0]
for _ in range(N):
    arr.append(int(input()))

dp = [0] * (N + 1)

dp[1], dp[2], dp[3] = arr[1], arr[1] + arr[2], max(arr[2] + arr[3], arr[1] + arr[3])

for i in range(4, N + 1):
    dp[i] = max(arr[i] + arr[i - 1] + dp[i - 3], arr[i] + dp[i - 2])
    
print(dp[N])