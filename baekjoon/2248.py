import sys
input = sys.stdin.readline

n, l, i = map(int, input().split())
dp = [[-1] * 33 for __ in range(33)]


def init(idx, limit):
    if limit == 0 or idx == n:
        return 1

    ret = dp[idx][limit]
    if ret != -1:
        return ret

    dp[idx][limit] = init(idx+1, limit-1) + init(idx+1, limit)
    return dp[idx][limit]


def binary(idx, limit, cnt):
    if idx == n:
        return ''

    ret = init(idx+1, cnt)

    if limit >= ret:
        return '1' + binary(idx+1, limit-ret, cnt-1)
    else:
        return '0' + binary(idx+1, limit, cnt)


print(binary(0, i-1, l))