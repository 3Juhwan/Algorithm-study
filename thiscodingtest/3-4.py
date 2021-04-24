N, K = map(int, input().split())
result = 0

while N > 1:
    if N < K:
        break
        
    target = N % K
    result += target
    N -= target
    
    N //= K
    result += 1

result += N - 1
print(result)