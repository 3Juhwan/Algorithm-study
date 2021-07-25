from sys import stdin
from collections import deque
input = stdin.readline
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

for _ in range(int(input())):
    h, w = map(int, input().split())
    a = [['.']+list(input().strip())+['.'] for _ in range(h)]
    a = ['.'*(w+2)] + a + ['.'*(w+2)]
    check = [[False]*(w+2) for _ in range(h+2)]
    keys = [False]*26
    k = input().strip()
    if k != '0':
        for t in k:
            keys[ord(t)-ord('a')] = True

    def bfs():
        q = deque()
        dq = [deque() for _ in range(26)]
        q.append((0, 0))
        check[0][0] = True
        ans = 0
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if nx < 0 or nx > h+1 or ny < 0 or ny > w+1:
                    continue
                if a[nx][ny] == '*' or check[nx][ny]:
                    continue
                check[nx][ny] = True
                if a[nx][ny] == '$':
                    ans += 1
                elif 'A' <= a[nx][ny] <= 'Z':
                    door = ord(a[nx][ny]) - ord('A')
                    if keys[door] is False:
                        dq[door].append((nx, ny))
                        continue
                elif 'a' <= a[nx][ny] <= 'z':
                    key = ord(a[nx][ny]) - ord('a')
                    keys[key] = True
                    while dq[key]:
                        kx, ky = dq[key].popleft()
                        q.append((kx, ky))
                q.append((nx, ny))
        return ans

    print(bfs())


# 출처: https://rebas.kr/660 [PROJECT REBAS]