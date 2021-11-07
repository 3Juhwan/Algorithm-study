from math import factorial, gcd
import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for __ in range(n)]
k = int(input())
NUM = (1<<n)-1

dp = [[-1]*k for __ in range(NUM+1)]
digit = [10**i for i in range(51)]
elen = [len(str(x)) for x in arr]


def answer(visited, remain):
    if visited == NUM:
        if remain == 0:
            return 1
        return 0

    if dp[visited][remain] != -1:
        return dp[visited][remain]

    result = 0
    for i in range(n):
        if visited & (1<<i) == 0:
            n_remain = (remain*digit[elen[i]] + arr[i]) % k
            result += answer(visited|(1<<i), n_remain)

    dp[visited][remain] = result
    return result


def getReduced(x, y):
    if x == 0: y = 1
    else:
        s = gcd(x, y)
        x, y = x//s, y//s
    print('{}/{}'.format(x, y))


result = answer(0, 0)
getReduced(result, factorial(n))