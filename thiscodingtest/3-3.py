N, M = map(int, input().split())
result = 0

for _ in range(N):
    data = list(map(int, input().split()))
    min_data = min(data)
    
    result = max(result, min_data)
    
print(result)