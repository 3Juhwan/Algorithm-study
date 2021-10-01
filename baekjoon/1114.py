import sys
input = sys.stdin.readline
L, K, C=map(int,input().split())
loc = list(sorted(map(int, input().split()))) + [L]
l, r = 0, L
while l <= r:
    x = (l+r)//2
    p, s, c = [0] * 3
    for i in range(K, -1, -1):
        d = loc[i]-loc[i-1] if i != 0 else loc[0]
        if d > x:
            c = C+1
            break
        if s+d > x:
            s, p = 0, i
            c += 1
        s += d
    if c > C:
        l = x+1
    else:
        a, r = x, x-1
        b = loc[p] if c == C else loc[0]
print(a, b)