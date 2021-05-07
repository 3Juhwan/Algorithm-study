K, N = map(int, input().split())
db = []
for _ in range(K):
    db.append(int(input()))

left, right = 1, sum(db) // N

while left <= right:
    mid = (left + right) // 2
    
    cnt = 0
    for data in db:
        cnt += data // mid
        
    if cnt >= N:
        left = mid + 1
    else:
        right = mid - 1
        
print(right)