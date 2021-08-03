from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, m = map(int, input().split())
a = [list(input().rstrip()) for _ in range(n)]
check = [[[[0] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

_rx, _ry, _bx, _by = [0] * 4
for i in range(n):
    for j in range(m):
        if a[i][j] == 'R':
            _rx, _ry = i, j
        elif a[i][j] == 'B':
            _bx, _by = i, j

q = deque([(_rx, _ry, _bx, _by, 0)])
check[_rx][_ry][_bx][_by] = 1

def move(_x, _y, _dx, _dy, _c):
    while a[_x+_dx][_y+_dy] != '#' and a[_x][_y] != 'O':
        _x += _dx
        _y += _dy
        _c += 1
    return _x, _y, _c

def bfs():
    while q:
        rx, ry, bx, by, d = q.popleft()
        if d >= 10:
            break
        for i in range(4):
            nrx, nry, rc = move(rx, ry, dx[i], dy[i], 0)
            nbx, nby, bc = move(bx, by, dx[i], dy[i], 0)
            if a[nbx][nby] == 'O':
                continue
            if a[nrx][nry] == 'O':
                print(1)
                return
            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx, nry = nrx-dx[i], nry-dy[i]
                else:
                    nbx, nby = nbx-dx[i], nby-dy[i]
            if not check[nrx][nry][nbx][nby]:
                check[nrx][nry][nbx][nby] = True
                q.append((nrx, nry, nbx, nby, d+1))
    print(0)

bfs()