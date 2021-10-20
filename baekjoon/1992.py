import sys
input = sys.stdin.readline

n = int(input())
shape = [list(input().rstrip()) for __ in range(n)]


def quadTree(x, y, n):
    if isCompress(x, y, n):
        return -1

    print('(', end='')

    for i in range(2):
        for j in range(2):
            quadTree(x+n//2*i, y+n//2*j, n//2)

    print(')', end='')


def isCompress(x, y, n):
    zero, one = [0]*2
    for i in range(x, x+n):
        for j in range(y, y+n):
            if shape[i][j] == '1':
                one += 1
            else:
                zero += 1
            if zero and one:
                return False

    print('1' if one else '0', end='')
    return True


quadTree(0, 0, n)