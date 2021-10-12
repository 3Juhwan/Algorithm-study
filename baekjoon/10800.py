from collections import Counter as C
import sys
input = sys.stdin.readline

n = int(input())
answer = [0] * n
ball = []        # 색, 크기, 순서
for i in range(n):
    x, y = map(int, input().split())
    ball.append((x, y, i))
ball.sort(key=lambda x: x[1], reverse=True)

dp = [0] * (n+1)
total, t_total = [0]*2
d = C()
i = 1
while ball:
    while ball[-1][1] != i:
        total += t_total
        for color, sum in d.most_common():
            dp[color] += sum * i
        d = C()
        t_total = 0
        i += 1
    color, size, idx = ball.pop()
    d[color] += 1
    answer[idx] = total - dp[color]
    t_total += size

for x in answer: print(x)