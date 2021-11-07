from math import gcd, factorial as f
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [[-1]*(m+1) for __ in range(n+1)]


def c(n, x):
    return f(n)//(f(n-x)*f(x))


def answer(n, b):
    if n == 0:
        return 1
    if b == 0:
        return 0

    if dp[n][b] != -1:
        return dp[n][b]

    ret = 0
    for i in range(1, n+1):
        tmp = answer(n-i, b-1) * c(n-1, i-1) * f(i-1)
        ret += tmp

    dp[n][b] = ret
    return ret


result = answer(n, m)

if result == 0:
    print('{}/{}'.format(0, 1))
else:
    t = gcd(result, f(n))
    print('{}/{}'.format(result//t, f(n)//t))