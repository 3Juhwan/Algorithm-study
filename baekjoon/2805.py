N, M = map(int, input().split())
H = list(map(int, input().split()))
start, end = 1, max(H)

while start <= end:
    mid = (start+end) // 2
    
    cutLen = sum(map(lambda x : x - mid if x - mid > 0 else 0, H))
    
    if cutLen >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)
