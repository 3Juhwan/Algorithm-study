n = int(input())
v = [[' ']*n*2 for __ in range(n)]


def draw(x, y, n):
    if n == 3:
        v[x][y] = '*'
        v[x+1][y-1], v[x+1][y+1] = ['*'] * 2
        v[x+2][y-2:y+3] = ['*']*5
        return 0

    mid = n//2

    draw(x, y, mid)
    draw(x+mid, y-mid, mid)
    draw(x+mid, y+mid, mid)


draw(0, n-1, n)

# 입출력보다 문자열 연산이 빠르다
for x in v:
	print(''.join(x))