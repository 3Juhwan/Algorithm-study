import sys
sys.setrecursionlimit(20000)
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [[-1]*101 for __ in range(10001)]


def rectangle(n, m):
    n, m = (m, n) if n < m else (n, m)

    if n == m:
        return 1

    if dp[n][m] != -1:
        return dp[n][m]

    ret = int(1e20)
    if n >= 3*m:
        ret = min(ret, rectangle(n-m, m)+1)
    else:
        for i in range(1, n//2+1):
            ret = min(ret, rectangle(i, m) + rectangle(n-i, m))
        for i in range(1, m//2+1):
            ret = min(ret, rectangle(n, i) + rectangle(n, m-i))

    dp[n][m] = ret
    return ret


print(rectangle(n, m))