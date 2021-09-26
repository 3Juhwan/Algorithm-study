import sys
input = sys.stdin.readline

answer = 0
n = int(input())
arr = [int(input()) for __ in range(n)]

q = [(arr[0], 0)]
for i in range(1, len(arr)):
    idx = i
    while q and q[-1][0] > arr[i]:
        num, idx = q.pop()
        answer = max(answer, num * (i-idx))
    q.append((arr[i], idx))

while q:
    num, idx = q.pop()
    answer = max(answer, num * (len(arr)-idx))

print(answer)