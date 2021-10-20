import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())
n = 1 << n

NUMBER = 0


def cntNum(x, y, n):
    global NUMBER, r, c

    if x == r and y == c:
        print(NUMBER)
        sys.exit()

    if x+n <= r or y+n <= c:
        NUMBER += n**2
        return 0

    for i in range(2):
        for j in range(2):
            cntNum(x+n//2*i, y+n//2*j, n//2)


cntNum(0, 0, n)