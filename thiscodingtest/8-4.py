N, M = map(int, input().split())
coin_type = []
for _ in range(N):
    coin_type.append(int(input()))

d = [-1] * 10001
coin_type.sort()  # 편의상 오름차순 정렬

for x in coin_type:
    d[x] = 1
    
for i in range(1, M + 1):
    for c in coin_type:
        idx = i - c
        
        # 돈 단위보다 구하는 값이 적은 경우, 탈출!! 
        if idx <= 0:
            break
        
        # 값을 구할 수 없는 경우, 다음 계속!
        if d[idx] == -1:
            continue
        
        val = d[idx] + 1
        
        if d[i] == -1:
            d[i] = val
        else:
            d[i] = min(d[i], val)
        
print(d[M])