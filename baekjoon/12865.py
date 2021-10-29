import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for __ in range(n)]
dp = [[-1] * 100001 for __ in range(101)]


def bag(x, w):
    if x == n:
        return 0

    ret = dp[x][w]
    if ret != -1:
        return ret

    ret = bag(x+1, w)
    if w >= arr[x][0]:
        ret = max(ret, arr[x][1] + bag(x+1, w-arr[x][0]))
    dp[x][w] = ret

    return ret


answer = 0
for i in range(n):
    answer = max(answer, bag(i, k))
print(answer)