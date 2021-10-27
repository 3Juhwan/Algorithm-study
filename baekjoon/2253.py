import sys
sys.setrecursionlimit(20000)
input = sys.stdin.readline

n, m = map(int, input().split())

visited = [1] * (n+1)
for __ in range(m):
    visited[int(input())] = 0

dp = [[-1] * 200 for __ in range(n+1)]


def answer(now, jump):
    if now == n:
        return 1 + dp[now][jump]

    if now > n or visited[now] == 0:
        return int(1e9)

    ret = dp[now][jump]
    if ret != -1:
        return 1 + ret

    ret = int(1e9)
    for i in range(-1, 2, 1):
        next = jump + i
        if next >= 1:
            ret = min(ret, answer(now+next, next))

    dp[now][jump] = ret
    return 1 + dp[now][jump]


result = answer(1, 0)
print(result if result < n else -1)