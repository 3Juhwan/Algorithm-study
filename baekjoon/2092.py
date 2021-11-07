import sys
sys.setrecursionlimit(5000)
input = sys.stdin.readline
MOD = int(1e6)

t, a, s, b = map(int, input().split())
left = [0] * 4001
for x in map(int, input().split()):
    left[x] += 1
dp = [[-1]*4001 for __ in range(201)]


def mkSet(n, cnt):
    if n == t:
        return (s <= cnt <= b)

    if dp[n][cnt] != -1:
        return dp[n][cnt]

    ret = 0
    for i in range(left[n+1]+1):
        ret = (ret + mkSet(n+1, cnt+i)) % MOD

    dp[n][cnt] = ret
    return ret


print(mkSet(0, 0))