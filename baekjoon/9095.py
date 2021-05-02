T = int(input())

for _ in range(T):
    N = int(input())
    
    d = [0] * 11
    d[1], d[2], d[3] = 1, 2, 4

    for i in range(4, N + 1):
        for j in range(1, 4):
            d[i] += d[i - j]

    print(d[N])