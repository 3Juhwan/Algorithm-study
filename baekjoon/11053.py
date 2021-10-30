
n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))



'''Recursion Code'''

n = int(input())
arr = list(map(int, input().split()))
dp = [-1] * n


def LIS(x):
    if x == n:
        return 1

    ret = dp[x]
    if ret != -1:
        return ret

    for i in range(x+1, n):
        if x == -1 or arr[x] < arr[i]:
            ret = max(ret, LIS(i))

    dp[x] = ret + 1
    return dp[x]


print(LIS(-1))