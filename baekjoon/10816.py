import sys

N = int(input())
com_data = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(input())
input_data = list(map(int, sys.stdin.readline().rstrip().split()))

arr = [0] * 20000001

for x in com_data:
    arr[x] += 1
    
for x in input_data:
    print(arr[x], end=' ')