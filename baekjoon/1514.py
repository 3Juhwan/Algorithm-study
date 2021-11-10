from math import ceil
import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().rstrip() + '000'))
e = list(map(int, input().rstrip() + '000'))
dp = [[[[-1]*10 for __ in range(10)] for __ in range(10)] for __ in range(n)]


def getP(x):
    return (x+10)%10


def getM(x):
    return int(ceil(x/3))


def answer(idx, s1, s2, s3):
    if idx == n:
        return 0

    if dp[idx][s1][s2][s3] != -1:
        return dp[idx][s1][s2][s3]

    ret = int(1e6)
    for i in (-1, 1):
        dif = getP(getP(e[idx]-s1) * i)
        for j in range(dif+1):
            for k in range(j+1):
                t1, t2 = getP(s2+j*i), getP(s3+k*i)
                ret = min(ret, getM(dif-j) + getM(j-k) + getM(k) + answer(idx+1, t1, t2, s[idx+3]))

    dp[idx][s1][s2][s3] = ret
    return ret


print(answer(0, s[0], s[1], s[2]))