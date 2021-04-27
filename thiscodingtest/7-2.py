N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = 'Out of stock'

start, end = 0, max(arr)  # 높이에 대한 변수
while start <= end:
    mid = (start + end) // 2
    sumOfRicecake = 0

    for d in arr:
        if d > mid:
            sumOfRicecake += d - mid

    if sumOfRicecake >= M:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)