import sys
input = sys.stdin.readline


def turnBulb(tmp, x):
	tmp[x-1] = not tmp[x-1]
	tmp[x] = not tmp[x]
	tmp[x+1] = not tmp[x+1]


n = int(input())
pre = list(map(int, list(input().rstrip()))) + [0]
aft = list(map(int, list(input().rstrip()))) + [0]
answer = int(1e9)

tmp = pre[:]

# 첫 번째 스위치를 누르지 않았을 때
cnt = 0
for i in range(1, n):
    if tmp[i-1] != aft[i-1]:
        turnBulb(tmp, i)
        cnt += 1

if tmp[n-1] == aft[n-1]:
    answer = min(cnt, answer)


tmp = pre[:]
tmp[0] = not tmp[0]
tmp[1] = not tmp[1]

# 첫 번째 스위치를 눌렀을 때
cnt = 1
for i in range(1, n):
    if tmp[i-1] != aft[i-1]:
        turnBulb(tmp, i)
        cnt += 1

if tmp[n-1] == aft[n-1]:
    answer = min(cnt, answer)

print(answer if answer != int(1e9) else -1)