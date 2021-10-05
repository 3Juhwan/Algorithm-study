n = int(input())
arr = [list(map(lambda x: int(x)//100*60+int(x)%100, input().split())) for __ in range(n)]
arr.sort()
for i in range(n):
    arr[i][0] -= 10
    arr[i][1] += 10

start, end = 10*60, 22*60
answer = 0
for s, e in arr:
    if s > start:
        answer = max(answer, s-start)
    start = max(start, e)
if end > start:
	answer = max(answer, end-start)
print(answer)