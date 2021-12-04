import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[-1, -1]] + [list(map(int, input().split())) for __ in range(n)]
dp = [[[-1]*2 for __ in range(1001)] for __ in range(1001)]
ssum = [0] * (n+1)

for i in range(1, n+1):
    ssum[i] = ssum[i-1] + arr[i][1]


def getMinCost(left, right, bool):
    if left == 1 and right == n:
        return 0

    if dp[left][right][bool] != -1:
        return dp[left][right][bool]

    now = right if bool else left
    rest = ssum[n]-ssum[right]+ssum[left-1]
    ret = int(1e20)
    if left > 1:
        dist = arr[now][0]-arr[left-1][0]
        ret = min(ret, rest*dist + getMinCost(left-1, right, 0))
    if right < n:
        dist = arr[right+1][0]-arr[now][0]
        ret = min(ret, rest*dist + getMinCost(left, right+1, 1))
        
    dp[left][right][bool] = ret
    return ret


print(getMinCost(m, m, 0))