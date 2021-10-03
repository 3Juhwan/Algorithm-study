n = int(input())
arr = []
for i, x in enumerate(map(int, input().split())):
	arr.insert(i-x, i+1)
print(*arr)