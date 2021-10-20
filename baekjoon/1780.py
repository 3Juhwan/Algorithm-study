import sys
input = sys.stdin.readline

n = int(input())
shape = [list(map(int, input().split())) for __ in range(n)]
papers = [0]*3


def cntVector(x, y, n):
    if isSame(x, y, n):
        return -1

    for i in range(3):
        for j in range(3):
            cntVector(x+n//3*i, y+n//3*j, n//3)


def isSame(x, y, n):
    zero, plus, minus = [0]*3
    for i in range(x, x+n):
        for j in range(y, y+n):
            if shape[i][j] == -1:
                minus += 1
            elif shape[i][j] == 0:
                zero += 1
            else:
                plus += 1
            if (zero and plus) or (zero and minus) or (plus and minus):
                return False

    if minus:
        papers[0] += 1
    elif zero:
        papers[1] += 1
    else:
        papers[2] += 1

    return True


cntVector(0, 0, n)
for p in papers: print(p)