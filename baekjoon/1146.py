import sys
input = sys.stdin.readline
MOD = 1_000_000

n = int(input())
dp = [[[-1]*2 for __ in range(n+1)] for __ in range(n+1)]


def answer(dir, l, r):
    if l+r == 0:
        return 1
    if dir == 0 and l == 0:
        return 0
    if dir == 1 and r == 0:
        return 0

    if dp[l][r][dir] != -1:
        return dp[l][r][dir]

    ret = 0
    if dir == 0:
        for i in range(l):
            ret += answer(not dir, i, r+l-i-1) % MOD
    if dir == 1:
        for i in range(r):
            ret += answer(not dir, l+i, r-i-1) % MOD

    dp[l][r][dir] = ret % MOD
    return ret % MOD


result = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if i < j:
            result += answer(0, j-2, n-j)
        if i > j:
            result += answer(1, j-1, n-j-1)
print(result % MOD if n != 1 else 1)