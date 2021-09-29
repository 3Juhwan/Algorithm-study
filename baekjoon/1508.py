import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
spots = list(map(int, input().split()))

answer = 0
start, end = 0, n
while start <= end:
    mid = (start + end) // 2
    visited = [0] * k
    s, cnt = [0] * 2
    for i in range(k):
        if cnt == m:
            break
        if spots[i] - spots[s] >= mid:
            visited[s] = 1
            s = i
            cnt += 1
    if cnt < m:
        visited[s] = 1
        cnt += 1

    if cnt > m:
        start = mid + 1
    elif cnt == m:
        answer = ''.join(str(v) for v in visited)
        start = mid + 1
    else:
        end = mid - 1

print(answer)