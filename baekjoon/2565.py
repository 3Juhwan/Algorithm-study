def dfs(idx, limit):
    if arr[idx][1] < limit:
        return 0

    if dp[idx][limit]:
        return dp[idx][limit]

    dp[idx][limit] = max([0] + [dfs(i, arr[idx][1] + 1) for i in range(idx + 1, n)]) + 1
    return dp[idx][limit]


n = int(input())
arr = [list(map(int, input().split())) for __ in range(n)]
arr.sort()

dp = [[0] * 501 for __ in range(501)]
answer = max([dfs(i, arr[i][1]) for i in range(n)])
print(n-answer)