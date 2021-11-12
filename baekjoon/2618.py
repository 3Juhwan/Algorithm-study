import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
w = int(input())
arr = [[1, 1]] + [list(map(int, input().split())) for __ in range(w)] + [[n, n]]
dp = [[-1]*1002 for __ in range(1002)]


def dist(a1, a2):
    x1, y1 = a1
    x2, y2 = a2
    return abs(x2-x1)+abs(y2-y1)


def police(x, a1, a2):
    if x == w:
        dp[a1][a2] = 0
        return 0

    if dp[a1][a2] != -1:
        return dp[a1][a2]

    dp[a1][a2] = min(dist(arr[a1], arr[x+1]) + police(x+1, x+1, a2), dist(arr[a2], arr[x+1]) + police(x+1, a1, x+1))

    return dp[a1][a2]


answer = police(0, 0, w+1)
print(answer)

s, e = 0, w+1
for i in range(1, w+1):
    if dist(arr[i], arr[e]) == dp[s][e]-dp[s][i]:
        print(2)
        e = i
        continue
    if dist(arr[i], arr[s]) == dp[s][e]-dp[i][e]:
        print(1)
        s = i
        continue