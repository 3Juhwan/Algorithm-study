import sys
input = sys.stdin.readline

t = int(input())
for __ in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for __ in range(n)]
    arr.sort()
    cnt = 1
    for i in range(n-1):
        if arr[i][1] > arr[i+1][1]:
            cnt += 1
        else:
            arr[i+1][1] = arr[i][1]
    print(cnt)