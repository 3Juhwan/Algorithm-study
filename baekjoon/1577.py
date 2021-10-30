import sys
input = sys.stdin.readline

n, m = map(int, input().split())
k = int(input())
ruin = []
for __ in range(k):
    a, b, c, d = map(int, input().split())
    ruin.append(sorted([(a, b), (c, d)]))

dp = [[-1] * (m+1) for __ in range(n+1)]


def distance(x, y):
    if x == n and y == m:
        return 1

    ret = dp[x][y]
    if ret != -1:
        return ret

    ret = 0
    if x < n:
        next = [(x, y), (x+1, y)]
        if next not in ruin:
            ret += distance(x+1, y)

    if y < m:
        next = [(x, y), (x, y+1)]
        if next not in ruin:
            ret += distance(x, y+1)

    dp[x][y] = ret
    return ret


print(distance(0, 0))