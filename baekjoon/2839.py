N = int(input())

m, n = 0, 0
flag = 0
mnum = int(N/3)

while m*5 <= N:
    while m*5+n*3 <= N:
        if m*5+n*3 == N and mnum >= m+n:
            mnum = m+n
            flag += 1
        n += 1
    m += 1
    n = 0

if flag == 0:
    mnum = -1
print(mnum)
