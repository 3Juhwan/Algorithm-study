import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for __ in range(n)]
arr.sort()

answer = 0
now = -1_000_000_000
for x, y in arr:
    if x >= now:
        answer += y - x
        now = y
    elif y >= now:
        answer += y - now
        now = y

print(answer)