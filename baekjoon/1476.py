e, s, m = map(int,input().split())
cnt = 1

while True:
    if e == 1 and s == 1 and m == 1:
        break
    
    e, s, m = e-1, s-1, m-1
    cnt += 1
    
    if e < 1:
        e = 15
    if s < 1:
        s = 28
    if m < 1:
        m = 19
    
print(cnt)
