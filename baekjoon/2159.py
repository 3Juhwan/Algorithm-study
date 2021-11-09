import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline
LIMIT = 100001

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n = int(input())
x, y = map(int, input().split())
arr = [list(map(int, input().split())) for __ in range(n)]
dp = [[-1]*4 for __ in range(n)]


def deliver(idx, cnt, x, y):
    if idx == n-1:
        return 0

    if dp[idx][cnt] != -1:
        return dp[idx][cnt]

    ret = int(1e20)
    for i in range(4):
        nx, ny = arr[idx+1][0]+dx[i], arr[idx+1][1]+dy[i]
        if 0 <= nx < LIMIT and 0 <= ny < LIMIT:
            ret = min(ret, abs(x-nx) + abs(y-ny) + deliver(idx+1, i, nx, ny))

    dp[idx][cnt] = ret
    return ret


print(deliver(-1, 0, x, y))