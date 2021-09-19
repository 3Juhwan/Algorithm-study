import sys
input = sys.stdin.readline

t = int(input())
for __ in range(t):
    n = int(input())
    answer = 0

    while n > 0:
        num = n % 100
        n //= 100

        dp = [100] * 100
        dp[0], dp[1], dp[10], dp[25] = 0, 1, 1, 1
        for i in range(1, num+1):
            dp[i] = min(dp[i], dp[i-1] + 1)
            dp[i] = min(dp[i], dp[i-10] + 1)
            dp[i] = min(dp[i], dp[i-25] + 1)

        answer += dp[num]

	print(answer)