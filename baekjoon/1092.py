import sys
from bisect import bisect_right

n = int(input())
crane = list(map(int, input().split()))
m = int(input())
box = [0] + list(map(int, input().split()))
crane.sort()
box.sort()

craneSite = [bisect_right(box, crane[i]) - 1 for i in range(n)]
boxNum = [craneSite[0]] + [craneSite[i] - craneSite[i - 1] for i in range(1, n)]

if m not in craneSite:
    print(-1)
    sys.exit()

limit, poss = 0, 0
for i in range(n - 1, -1, -1):
    left = boxNum[i] - limit
    if left <= 0:
        poss -= left
        continue
    while left > poss:
        poss += (n - i)
        limit += 1
    poss -= left
print(limit)