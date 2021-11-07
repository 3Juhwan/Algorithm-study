import sys
sys.setrecursionlimit(5000)
input = sys.stdin.readline

n, l = map(int, input().split())
arr = [int(input()) for __ in range(n)] + [l]
arr.sort()
n += 1
dp = [[-1]*1001 for __ in range(1001)]


def answer(i, j):
    l, r = (i, j) if i < j else (j, i)

    if l == 0 and r == n-1:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    ret = int(1e13)
    num = n-(r-l+1)
    if l > 0:
        now = (arr[i] - arr[l-1]) * num
        ret = min(ret, now + answer(l-1, r))
    if r < n-1:
        now = (arr[r+1] - arr[i]) * num
        ret = min(ret, now + answer(r+1, l))

    dp[i][j] = ret
    return ret


s = arr.index(l)
print(answer(s, s))