import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

answer = 0

pivot = 0
while len(arr) > pivot and arr[pivot] < 0:
	pivot += 1

for i in range(0, pivot, m):
	answer -= 2 * arr[i]
for i in range(n-1, pivot - 1, -m):
	answer += 2 * arr[i]

answer -= abs(max(abs(arr[0]), abs(arr[-1])))

print(answer)