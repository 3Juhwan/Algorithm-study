import sys
sys.setrecursionlimit(3000)
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [[-1] * (n+1) for __ in range(n+1)]
maxdp = [[0] * n for __ in range(n)]
mindp = [[int(1e9)] * n for __ in range(n)]

for i in range(n):
    for j in range(i, n):
        maxdp[i][j] = max(maxdp[i][j-1], arr[j])

for i in range(n):
    for j in range(i, n):
        mindp[i][j] = min(mindp[i][j-1], arr[j])


def group(idx, num):
    if idx >= n or num == 0:
        return 0

    ret = dp[idx][num]
    if ret != -1:
        return ret

    ret = 0
    for i in range(num):
        diff = maxdp[idx][idx+i] - mindp[idx][idx+i]
        ret = max(ret, group(idx+i+1, num-i-1) + diff)

    dp[idx][num] = ret
    return ret


print(group(0, n))