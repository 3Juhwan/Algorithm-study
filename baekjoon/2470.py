from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

answer = []
digit = int(1e12)

for i in range(n):
    x = -arr[i]
    idx = bisect_left(arr, x)
    if idx == 0:
        if digit > abs(x-arr[0]) and i != 0:
            digit = abs(x-arr[0])
            answer = [arr[0], arr[i]]

    elif idx == n:
        if digit > abs(x-arr[-1]) and i != n-1:
            digit = abs(x-arr[-1])
            answer = [arr[i], arr[-1]]

    else:
        if digit > abs(x-arr[idx]) and i != idx:
            digit = abs(x-arr[idx])
            answer = [arr[i], arr[idx]]
        if digit > abs(x-arr[idx-1]) and i != idx-1:
            digit = abs(x-arr[idx-1])
            answer = [arr[i], arr[idx-1]]

answer = answer if answer[0] < answer[1] else (answer[1], answer[0])
print(*answer)