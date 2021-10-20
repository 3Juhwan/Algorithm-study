n = int(input())
shape = [['*']*n for __ in range(n)]


def color(x, y, n):
    if n == 1:
        return -1

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                blank(x+n//3*i, y+n//3*j, n//3)
            else:
                color(x+n//3*i, y+n//3*j, n//3)


def blank(x, y, n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            shape[i][j] = ' '

color(0, 0, n)

for g in shape:
    for x in g:
        print(x, end='')
	print()