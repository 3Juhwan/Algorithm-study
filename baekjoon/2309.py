import sys
input = sys.stdin.readline

arr = [int(input()) for __ in range(9)]
total = sum(arr)
arr.sort()
diff = total - 100

for i in range(8):
	for j in range(i+1, 9):
        if arr[i] + arr[j] == diff:
            del arr[i]
            del arr[j-1]

            for x in arr:
                print(x)
            sys.exit()