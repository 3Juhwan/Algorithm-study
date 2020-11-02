N, m, M, T, R = map(int, input().split())
work_out = 0
cnt = 0
status = m

if status + T > M:
    cnt = -1
    work_out = N

while work_out < N:
    if status + T <= M:
        status += T
        work_out += 1
    else:
        status -= R
    if status < m:
        status = m
    cnt += 1

print(cnt)
